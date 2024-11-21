# Person Detection on Raspberry Pi 4 Model B

This project implements real-time person detection on a Raspberry Pi 4 using YOLOv5 Nano and the Raspberry Pi 5mp Camera Module. It processes live video feeds and identifies persons in the frame using lightweight object detection.

## Features
- Real-time object detection using YOLOv5 Nano.
- Filters for detecting only persons (class 0).
- Saves detected frames with bounding boxes and confidence scores.
- Runs efficiently on Raspberry Pi 4 with low latency.

## Prerequisites
Before running the project, ensure the following are installed on your Raspberry Pi:
- **Python 3.7+**
- **Pipenv or Virtualenv**
- **YOLOv5**
- **libcamera**

### Python Libraries
- numpy
- opencv-python
- torch
