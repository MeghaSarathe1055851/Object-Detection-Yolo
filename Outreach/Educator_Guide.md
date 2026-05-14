# Educator Guide  
## AI Object Detection Workshop (Offline with Raspberry Pi + YOLO)

---

## Purpose of This Module

This activity is designed to introduce students to the concept of object detection using Artificial Intelligence in a fully offline and guided environment. The goal is not only for students to run a model, but to understand how AI learns from data, why it sometimes fails, and how the quality and quantity of data influence performance.

Throughout the session, students will go through the complete lifecycle of an AI system: collecting images, labeling them, training a model, and testing it in real-world scenarios. By the end, they should be able to explain how object detection works at a conceptual level and reflect on its limitations.

---

## Instructor Preparation

Before conducting the session, ensure that each system is properly set up with Python, YOLOv8, LabelImg, and the required scripts (`capture_app.py`, `training_app.py`, and `detection_app.py`). The working directory should already contain a `dataset` folder with two subfolders named `images` and `labels`.

It is important that the educator runs each component once before the class begins. This is not just to verify that the system works, but also to understand what students will experience at each stage.

Start by running the capture application and confirm that images can be taken and saved correctly in the `dataset/images` folder. Next, open the labeling tool and ensure that images load properly, bounding boxes can be drawn, and label files are saved into `dataset/labels`. Then, run the training application and observe how the dataset is split, how training progresses, and where the trained model is stored (typically inside the `runs/detect/train` directory). Finally, run the detection application and confirm that the model can detect objects using the camera in real time.

By going through this process once, the educator will be able to guide students more confidently and troubleshoot issues quickly during the session.

---

## How to Conduct the Activity

The activity should be delivered as a guided experience where students are encouraged to observe, question, and reflect at each stage rather than simply follow instructions.

The session begins with image collection. Students should select a simple object and capture multiple images of it using the capture application. They should be encouraged to vary the angle, distance, and lighting conditions. This step is essential because it introduces the idea that AI models require diverse data in order to generalize well.

Next comes labeling. This is where students define what the object is and where it appears in each image. It is important to explain that the bounding box represents the region of interest and that the label provides meaning to that region. Emphasize that incorrect labeling will directly affect how the model learns.

Once the dataset is labeled, students move on to training. At this stage, they will use the training application to experiment with different dataset sizes, typically comparing results from using 3 images per class versus 7 images per class. This is a critical learning moment. Students should be asked to predict which model will perform better and why. During this discussion, introduce the idea that the model starts by learning random patterns and gradually develops meaningful features such as edges, shapes, and textures.

After training, students test their model using the detection application. They should first present objects that were part of the training data and observe how well the model detects them. Then, they should present new objects that the model has never seen. This usually leads to incorrect detections or confusion, which helps students understand that AI systems are not inherently intelligent but are limited by their training data.

---

## What Students Should Learn

By the end of the activity, students should clearly understand that AI models learn from examples rather than rules. They should recognize that better and more varied data leads to better performance, and that poor or limited data leads to errors. They should also understand that AI systems can make mistakes, especially when encountering unfamiliar inputs.

---

## Guiding Student Thinking

Throughout the activity, the educator should continuously prompt students to think about why the model behaves the way it does. Instead of focusing on whether the model works, the focus should be on understanding its behavior.

Encourage students to think about questions such as why more images improve performance, why incorrect labels cause problems, and why the model fails on new objects. These discussions are more important than the technical steps themselves.

---

## Expected Challenges and How to Handle Them

Students may encounter situations where the model does not detect objects correctly, detects the wrong object, or fails entirely. These moments should be treated as learning opportunities rather than errors.

If detection is poor, guide students to consider whether they collected enough images or whether the images were diverse. If the model makes incorrect predictions, ask them to review their labeling. If the model struggles with new objects, use that as a way to explain how AI depends on training data and does not truly “understand” the world.

---

## Final Outcome

At the conclusion of the activity, students will have built and tested their own object detection system. More importantly, they will have gained an intuitive understanding of how AI models are trained, how they make predictions, and why they are not always reliable.

This activity is designed to move beyond simply running code and instead help students develop a deeper understanding of how artificial intelligence works in practice.