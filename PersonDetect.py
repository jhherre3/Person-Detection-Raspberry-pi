import subprocess
import numpy as np
import torch
from datetime import datetime
import cv2

# User-configurable settings
YOLO_MODEL = 'yolov5n'  # YOLOv5 model to use ('yolov5n', 'yolov5s', etc.)
SAVE_DIRECTORY = '/path/to/your/save/directory'  # Replace with your preferred save directory
FRAME_WIDTH = 320  # Width of the video frame
FRAME_HEIGHT = 240  # Height of the video frame
FRAMERATE = 15  # Frame rate of the video feed
PROCESS_EVERY_NTH_FRAME = 3  # Process every Nth frame for performance

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', YOLO_MODEL, pretrained=True).eval()

# Command to start libcamera-vid and output MJPEG stream
command = [
    'libcamera-vid',
    '-t', '0',                     # Run indefinitely
    '--width', str(FRAME_WIDTH),   # Set resolution
    '--height', str(FRAME_HEIGHT),
    '--framerate', str(FRAMERATE),
    '--codec', 'mjpeg',            # Use MJPEG for compatibility with OpenCV
    '--nopreview',                 # Disable preview window to reduce load
    '-o', '-',                     # Output to stdout
]

# Start the video capture process using libcamera
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=10**8)

# OpenCV capture loop
jpeg_bytes = b""
frame_count = 0

while True:
    try:
        # Read the MJPEG stream byte by byte
        chunk = process.stdout.read(4096)
        if not chunk:
            print("Failed to grab frame")
            break

        jpeg_bytes += chunk

        # Look for the JPEG end marker (0xFFD9)
        a = jpeg_bytes.find(b'\xff\xd9')
        if a != -1:
            # Extract the complete JPEG image
            jpg = jpeg_bytes[:a + 2]
            jpeg_bytes = jpeg_bytes[a + 2:]

            # Decode the JPEG image into an OpenCV frame
            np_arr = np.frombuffer(jpg, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Skip frames for faster processing
            frame_count += 1
            if frame_count % PROCESS_EVERY_NTH_FRAME != 0:
                continue

            # Resize frame before passing to YOLO for faster processing
            resized_frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

            # Run YOLOv5 on the frame
            results = model(resized_frame)

            # Filter results to only show "person" class (class 0)
            for i in range(len(results.xyxy[0])):
                if results.names[int(results.xyxy[0][i, -1])] == 'person':
                    # Draw the bounding box and label on the frame
                    x1, y1, x2, y2, conf, cls = results.xyxy[0][i]
                    cv2.rectangle(resized_frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    label = f"{results.names[int(cls)]} {conf:.2f}"
                    cv2.putText(resized_frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Live Feed with Person Detection', resized_frame)

            # Save the frame when 's' is pressed
            if cv2.waitKey(1) & 0xFF == ord('s'):
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                save_path = f"{SAVE_DIRECTORY}/person_detect_{timestamp}.jpg"
                cv2.imwrite(save_path, resized_frame)
                print(f"Image saved with person detection at {save_path}")

            # Quit the video feed when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Error: {e}")
        break

# Cleanup
process.terminate()
cv2.destroyAllWindows()
