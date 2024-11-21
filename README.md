# Person Detection on Raspberry Pi 4 Model B

This project implements real-time person detection on a Raspberry Pi 4 Model B using YOLOv5 Nano and the Raspberry Pi 5MP Camera Module. It processes live video feeds and identifies persons in the frame using lightweight object detection.

## Features
- Real-time object detection using YOLOv5 Nano.
- Filters detections to display only persons (class 0).
- Saves detected frames with bounding boxes and confidence scores.

### Hardware Requirements
- Raspberry Pi 4 Model B
- Raspberry Pi 5MP Camera Module (or compatible camera)
- Internet connection for downloading YOLOv5 model

### Software Requirements
- **Python 3.7+**
- **Pipenv or Virtualenv** (optional for managing dependencies)
- **YOLOv5**
- **libcamera**

### Required Python Libraries
Make sure the following Python libraries are installed:
- `numpy`
- `opencv-python`
- `torch`

You can install them using the following command:
```bash
pip install numpy opencv-python torch
