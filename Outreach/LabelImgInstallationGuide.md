# LabelImg Installation and Usage Guide  
## Offline Image Labeling for AI Object Detection (Raspberry Pi)

---

## Overview

This guide explains how to install and use LabelImg on a Raspberry Pi for labeling images in an offline object detection workflow.

LabelImg is used to create bounding box annotations for images, which are required for training the YOLO object detection model. This guide is part of the complete setup for the AI Object Detection learning module and is designed to work without requiring internet access after installation.

---

## System Requirements

Before installing LabelImg, ensure the system meets the following requirements:

- Raspberry Pi OS (64-bit)
- Python 3.9 or higher
- Required system libraries installed (see Technical Setup Guide)

---

## Installation Steps

LabelImg is installed locally on the Raspberry Pi using system packages and a Git repository.

### Step 1: Install Required System Packages

Run the following command to install dependencies:

```bash
sudo apt update
sudo apt install python3-pyqt5 pyqt5-dev-tools python3-lxml python3-pil git -y
```
