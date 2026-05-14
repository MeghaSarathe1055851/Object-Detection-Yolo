# Technical Setup Guide  
## AI Object Detection Workshop (Raspberry Pi – Offline Setup)

---

## Overview

This guide provides all the necessary steps to prepare a Raspberry Pi environment for running the AI Object Detection learning module. The setup is designed to work completely offline after installation, ensuring it is suitable for classroom environments without internet dependency.

The goal of this setup is to ensure that all required tools, libraries, and directory structures are ready before students begin the activity.

---

## Operating System

The system should be running:

**Raspberry Pi OS (64-bit)**

It is recommended to use an updated version of the OS to avoid compatibility issues with Python libraries and camera support.

To verify the OS version, you can run:

```uname -a```

## Python Environment

This project requires: Python 3.9 or higher
To check the installed version:

```python3 --version```

If Python is not installed or needs to be updated:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

**Required Libraries and Dependencies**

Install the required Python libraries using pip:

```bash
pip install ultralytics opencv-python pillow lxml
```

## Explanation of Libraries
ultralytics: Used for training and running the YOLO object detection model
opencv-python: Used for capturing images and displaying detection results
pillow: Supports image processing
lxml: Required for LabelImg functionality
Labeling Tool Setup (LabelImg)

LabelImg is used for labeling images locally without requiring internet access.

Installation Steps
```bash
sudo apt install python3-pyqt5 pyqt5-dev-tools git -y
git clone https://github.com/tzutalin/labelImg.git
cd labelImg
pyrcc5 -o libs/resources.py resources.qrc
python3 labelImg.py
```

Once installed, LabelImg can be used to:

- Open images
- Draw bounding boxes
- Save labels in YOLO format
- Project Directory Structure

Before running the learning module, ensure the following directory structure is created:

```bash
project_root/
├── dataset/
│   ├── images/
│   ├── labels/
│
├── apps/
│   ├── capture_app.py
│   ├── training_app.py
│   ├── detection_app.py
│
├── docs/
│   ├── Educator_Guide.md
│   ├── ObjectDetectionLearningModule.md
│   ├── LabelImgInstallationGuide.md

```

## Explanation
dataset/images/ → Stores captured images
dataset/labels/ → Stores corresponding label files
apps/ → Contains all Python scripts used in the activity
docs/ → Contains all instructional materials
Camera Setup

Ensure that the Raspberry Pi camera or USB webcam is properly connected and working.

## To test the camera:

```python3 -c "import cv2; cap=cv2.VideoCapture(0); print(cap.isOpened())```

If the output is True, the camera is working correctly.

## Running the Applications

All applications should be run from the project root directory.

## Capture Images

```bash
python capture_app.py
```
Images will be saved in: dataset/images/

## Label Images
```bash
python labelImg.py
```
Open images from dataset/images/ and Save labels to dataset/labels/

## Train the Model
```bash
python training_app.py
```
Select data set size (3 or 7 images per class).
Model will be trained automatically and then
Run Object Detection
```bash
python detection_app.py
```

Select trained model file then
Camera will open and show detections
