# Gesture-Controlled Volume Adjustment with MediaPipe and Python

This Python script allows you to control the volume of your PC using hand gestures detected by the MediaPipe library. It captures your webcam feed and adjusts the volume based on your thumbs-up and thumbs-down gestures.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- pycaw

You can install the required Python packages using pip:

```bash
pip install opencv-python mediapipe pycaw
```

Usage
Connect a webcam to your PC.

Run the Python script:

bash
Copy code
python volume_control.py
Place your hand in front of the webcam.

Show a thumbs-up gesture to increase the volume.

Show a thumbs-down gesture to decrease the volume.

No gesture will maintain the current volume.

Code Explanation
The script uses the MediaPipe library to detect hand landmarks.
It checks for thumbs-up and thumbs-down gestures.
When a thumbs-up gesture is detected, the script increases the volume.
When a thumbs-down gesture is detected, the script decreases the volume.
The volume changes in small increments to avoid sudden loudness changes.
The script also provides real-time feedback on the screen.
Customization
You can customize the following parameters in the script:
volume_change: Adjust the volume change per gesture.
Known Issues
If the script doesn't change the volume, ensure you have the required packages installed and that your microphone and speakers are correctly configured.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
MediaPipe
pycaw
Author
Dron Vyas

Feel free to contribute and improve this project!
