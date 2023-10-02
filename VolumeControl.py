import mediapipe as mp
import cv2
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
thumb_up_detected = False
thumb_down_detected = False
volume_change = 0.05 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error opening camera!")
        break
    
    frame_flip = cv2.flip(frame, 1)
    frame_RGB = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_RGB)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            landmarks_list = []
            for landmark in landmarks.landmark:
                landmarks_list.append((landmark.x, landmark.y, landmark.z))
            
            thumb_x, thumb_y, _ = landmarks_list[4]
            index_x, index_y, _ = landmarks_list[8]

            thumb_up = thumb_y < index_y
            thumb_down = thumb_y > index_y

            if thumb_up and not thumb_down_detected:
                cv2.putText(frame, 'thumbs up', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                current_volume = volume.GetMasterVolumeLevelScalar()
                new_volume = min(current_volume + volume_change, 1.0)
                volume.SetMasterVolumeLevelScalar(new_volume, None)
                thumb_up_detected = True
                thumb_down_detected = False
            elif thumb_down and not thumb_up_detected:
                cv2.putText(frame, 'thumbs down', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 0, 255), 2)
                current_volume = volume.GetMasterVolumeLevelScalar()
                new_volume = max(current_volume - volume_change, 0.0)
                volume.SetMasterVolumeLevelScalar(new_volume, None)
                thumb_down_detected = True
                thumb_up_detected = False
            else:
                thumb_up_detected = False
                thumb_down_detected = False
            
    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
