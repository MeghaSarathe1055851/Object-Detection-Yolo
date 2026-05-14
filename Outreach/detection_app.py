import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

def select_model():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select YOLO Model (.pt)")
    return file_path

model_path = select_model()

if not model_path:
    print("No model selected. Exiting...")
    exit()

model = YOLO(model_path)

cap = cv2.VideoCapture(0)

print("Press SPACE to continue, ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    cv2.imshow("Detection", annotated)

    key = cv2.waitKey(1)

    if key == 32:  # SPACE
        continue
    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()