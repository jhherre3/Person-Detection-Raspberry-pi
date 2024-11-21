# Raspberry Pi 4 Model B Person Detection Setup

This guide walks you through setting up a brand-new Raspberry Pi 4 Model B to run a YOLOv5-based person detection script. The instructions assume you are starting with a fresh Raspberry Pi OS installation.

---

## **Step 1: Update and Upgrade the System**

Update your Raspberry Pi to ensure it has the latest software:
```bash
sudo apt update && sudo apt upgrade -y

## **Step 2: Enable Camera**

sudo raspi-config

Navigate to Interface Options > Camera > Enable.
Reboot the Raspberry Pi to apply changes

sudo reboot

Step 3: Install Required Tools and Libraries
Install Python and Virtual Environment tools:

bash
Copy code
sudo apt install python3 python3-pip python3-virtualenv -y
Install additional Python libraries for the project:

bash
Copy code
pip3 install numpy opencv-python torch


Step 4: Set Up YOLOv5
Create a virtual environment for YOLOv5:

bash
Copy code
python3 -m venv ~/yolov5-env
source ~/yolov5-env/bin/activate
Clone the YOLOv5 repository:

bash
Copy code
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

Step 5: Add the Person Detection Script
Create the person_detect.py file:

bash
Copy code
nano ~/yolov5/person_detect.py
Copy and paste the script into the file. Save and exit:

Press CTRL+O to save.
Press Enter to confirm the filename.
Press CTRL+X to exit.
Step 6: Run the Person Detection Script
Activate the virtual environment:

bash
Copy code
source ~/yolov5-env/bin/activate
Navigate to the YOLOv5 directory:

bash
Copy code
cd ~/yolov5
Run the detection script:

bash
Copy code
python3 person_detect.py
Step 7: Interact with the Detection Script
Save a Frame:
Press S to save the current frame with detections. Saved images are stored in: /home/pi/Pictures/person_detect_<timestamp>.jpg.

Quit the Program:
Press Q to stop the detection and close the video feed.

Troubleshooting
Camera Not Working
Ensure the camera is properly connected.
Verify that the camera module is enabled:
bash
Copy code
sudo raspi-config
Low FPS
Reduce the resolution and frame rate in the script:
python
Copy code
'--width', '320',
'--height', '240',
'--framerate', '15',
Virtual Environment Not Found
Always activate the virtual environment before running the script:
bash
Copy code
source ~/yolov5-env/bin/activate
Optional Enhancements
Run on Boot:
Automate the script using cron or a systemd service.

Performance Optimization:
Convert the YOLOv5 model to TensorFlow Lite or use ONNX Runtime.

Logging:
Add logging to track detected objects and confidence levels over time.

By following these steps, you’ll have a fully functional person detection system running on your Raspberry Pi 4 Model B.
