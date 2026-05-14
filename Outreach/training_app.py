import os
import shutil
import random
import tkinter as tk
from tkinter import messagebox
from ultralytics import YOLO

DATASET_PATH = "dataset"
SPLIT_PATH = "dataset_split"

TRAIN_PATH = f"{SPLIT_PATH}/train"
TEST_PATH = f"{SPLIT_PATH}/test"

CLASSES = ["binder_clip", "book", "calculator", "highlighter",
           "notebook", "pen", "ruler", "stapler", "sticky_notes"]


def prepare_dataset(images_per_class):
    if os.path.exists(SPLIT_PATH):
        shutil.rmtree(SPLIT_PATH)

    os.makedirs(TRAIN_PATH + "/images")
    os.makedirs(TRAIN_PATH + "/labels")
    os.makedirs(TEST_PATH + "/images")
    os.makedirs(TEST_PATH + "/labels")

    images = os.listdir("dataset/images")

    class_groups = {cls: [] for cls in CLASSES}

    for img in images:
        label_file = f"dataset/labels/{img.replace('.jpg','.txt')}"
        if not os.path.exists(label_file):
            continue

        with open(label_file, "r") as f:
            class_id = int(f.readline().split()[0])
            class_name = CLASSES[class_id]
            class_groups[class_name].append(img)

    selected = []
    for cls in class_groups:
        selected += random.sample(class_groups[cls], min(images_per_class, len(class_groups[cls])))

    random.shuffle(selected)

    split = int(0.8 * len(selected))
    train_imgs = selected[:split]
    test_imgs = selected[split:]

    for img_list, dest in [(train_imgs, TRAIN_PATH), (test_imgs, TEST_PATH)]:
        for img in img_list:
            shutil.copy(f"dataset/images/{img}", f"{dest}/images/{img}")
            shutil.copy(f"dataset/labels/{img.replace('.jpg','.txt')}", f"{dest}/labels/{img.replace('.jpg','.txt')}")

    with open(f"{SPLIT_PATH}/data.yaml", "w") as f:
        f.write(f"""
train: {TRAIN_PATH}/images
val: {TEST_PATH}/images

nc: {len(CLASSES)}
names: {CLASSES}
""")


def evaluate_model(model):
    results = model.val(data=f"{SPLIT_PATH}/data.yaml")
    return results.box.map50  # simple accuracy metric


def train_model(images_per_class):
    prepare_dataset(images_per_class)

    model = YOLO("yolov8n.pt")

    model.train(
        data=f"{SPLIT_PATH}/data.yaml",
        epochs=30,
        imgsz=640
    )

    accuracy = evaluate_model(model)

    messagebox.showinfo("Training Complete", f"Model Accuracy (mAP@50): {accuracy:.2f}")


# GUI
root = tk.Tk()
root.title("Training App")

tk.Label(root, text="Select Images per Class").pack()

tk.Button(root, text="3 Images", command=lambda: train_model(3)).pack(pady=10)
tk.Button(root, text="7 Images", command=lambda: train_model(7)).pack(pady=10)

root.mainloop()