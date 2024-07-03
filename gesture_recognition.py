import cv2
import mediapipe as mp
import math
import numpy as np
from RobotHandGestures import utlis

# Importing serial library to communicate with Arduino
import serial

##############################################################################

# Set up parameters
cameraNo = 0
portNo = "COM4"
# cropVals = 100, 100, 300, 400  # StartPointY StartPointX h 
frameWidth = 640
frameHeight = 480
brightnessImage = 230

ser = serial.Serial(portNo, 9600)

cap = cv2.VideoCapture(cameraNo)
cap.set(10, brightnessImage)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

finger_cord = [(4, 5), (8, 6), (12, 10), (16, 14), (20, 18)]
finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
up_fingers = []

while True:
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        handList = []
        up_fingers = []
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))

            for i, coordinate in enumerate(finger_cord):
                if len(handList) >= 21:
                    if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                        up_fingers.append(finger_names[i])

    up_text = ", ".join(up_fingers) if up_fingers else "None"
    count_text = f"Up Fingers: {up_text}"
    cv2.putText(image, count_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    fingers_binary = [1 if finger in up_fingers else 0 for finger in finger_names]
    utlis.sendData(fingers_binary)
    print(fingers_binary)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
