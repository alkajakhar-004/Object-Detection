# YOLOv8 Real-Time Object Detection

This project implements a real-time object detection system using the Ultralytics YOLOv8 model on the COCO128 dataset with live webcam input.

## Features

- Real-time detection on webcam frames using YOLOv8.
- Pretrained yolov8n.pt model fine-tuned on COCO128 dataset.
- Bounding boxes, class labels, and confidence scores drawn directly on video frames.
- Adjustable confidence threshold for filtering detections.

## Tech Stack

- *Language:* Python 3.11
- *Deep Learning:* Ultralytics YOLOv8 (PyTorch backend) [web:230][web:76]
- *Computer Vision:* OpenCV-Python for webcam capture and display [web:138][web:142]
- *Environment:* Anaconda / Conda virtual environment [web:198]
- *IDE:* Visual Studio Code
- *Dataset:* COCO128 (subset of MS COCO – Common Objects in Context) [web:161][web:162]

## Installation

1. Conda environment banao aur activate karo:
Isme ultralytics, opencv-python, torch, aur numpy<2 jaisi libraries include hain. [web:230][web:135]

## Training (optional)

Agar model ko dobara train / fine-tune karna ho:
Is command se YOLOv8 COCO128 dataset par train hota hai aur best weights runs/detect/train/weights/best.pt me save hote hain. [web:97][web:74]

## Run Real-Time Detection

Webcam detection script chalane ke liye:
Script:

- cv2.VideoCapture(0) se default camera open karta hai.
- Har frame par model(frame, conf=0.5) se detection chalata hai. [web:230]
- results[0].plot() se boxes + labels draw karta hai. [web:230]
- cv2.imshow("YOLOv8 Live", annotated) window dikhata hai.
- ESC dabane par loop break ho jata hai aur camera close ho jata hai. [web:138]

## Future Work

- Video file input ka option add karna.
- Custom dataset ke saath training (apni classes). [web:74]
- FPS measurement aur performance comparison CPU vs GPU. [web:76]
"# Object-Detection" 
