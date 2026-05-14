import cv2
import os

SAVE_PATH = "dataset/images"
os.makedirs(SAVE_PATH, exist_ok=True)

# FIX: continue count from existing images
existing_images = [f for f in os.listdir(SAVE_PATH) if f.endswith(".jpg")]
count = len(existing_images)

cap = cv2.VideoCapture(0)

print("Press 'c' to capture image, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Images", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        img_name = f"{SAVE_PATH}/img_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved {img_name}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
