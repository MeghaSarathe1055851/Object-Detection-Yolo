# AI Object Detection Workshop

## Overview
In this activity, you will build an AI system that can detect objects using YOLO.

---

## Challenge 1 — Understanding Object Detection

Object detection works by identifying patterns (features) in images.

These features include:
- Edges
- Colors
- Textures

In YOLO:
- The model starts with random features
- During training, it learns ~64 filters
- These filters detect patterns like edges and shapes

### Question:
Which objects do you think would be easier to detect?

---

## Challenge 2 — Collecting Training Images

### Instructions:
1. Choose ONE object (e.g., pen)
2. Take **10 images**
3. Vary:
   - angle
   - lighting
   - background

### Run:
python capture_app.py

---

## Challenge 3 — Labeling Images

### Location of Tool:
labelImg.py (inside labeling_tool folder)

### Steps:
1. Open dataset/images
2. Save labels to dataset/labels
3. Draw bounding boxes
4. Assign labels

---

## Challenge 4 — Training

### Important:
Before training:
- Combine all labeled images
- Use USB if needed

### Directory:
dataset/
  images/
  labels/

### Run:
python training_app.py

Choose:
- 3 images OR 7 images per class

---

## Challenge 5 — Detection

Run:
python detection_app.py

### Controls:
- SPACE → next frame
- ESC → exit

---

## Recording Results

| Object Shown | Detected Object | Notes |
|-------------|---------------|------|
| pen         | pen           | correct |
| stapler     | notebook      | incorrect |

---

## Reflection

1. Why does AI need labeled data?
2. Why does more data improve accuracy?
3. Why does AI fail on new objects?