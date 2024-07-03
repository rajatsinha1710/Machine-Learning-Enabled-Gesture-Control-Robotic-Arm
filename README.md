
# Gesture Controlled Robotic Arm

In this project, we focused on closely replicating the human hand gestures and were able to replicate each finger movement independently which gave us freedom to make any kind of gesture by controlling each finger individually. Some of the key insights from the thesis are as follows:
1. Leveraged the Mediapipe framework, renowned for its robustness in landmark detection, to meticulously identify key landmarks on the hand.
2. Developed bespoke algorithms tailored to analyze the changes in finger length over time.
3. Implemented the Python serial module to establish a seamless communication channel between our Python-based gesture recognition system and the Arduino microcontroller responsible for controlling the robotic arm's servo motors. This integration facilitated real-time data transmission, enabling the Arduino to translate detected gestures into corresponding motor commands swiftly and accurately.
4. Through meticulous assembly and calibration, integrated the various components of the robotic arm, ensuring precise alignment and functionality. 

By meticulously connecting the motors to the Arduino and fine-tuning their responses, we achieved a high degree of fidelity in replicating human hand movements, thereby realizing the full potential of our Gesture Control Robotic Arm.



## Documentation

[Complete Documentaion on this Project](https://drive.google.com/file/d/1g5TAlvwyVkIMk6tyrY_4W9tZCPdWJV1m/view?usp=sharing)


## Deployment

1) install these modules numpy, pandas, mediapipe, OpenCV, serial, serialDevice

2) run the gesture_recognition.py this will open a window from your inbuilt camera if you are using external camera change "cameraNo" to 1.

3) connect the motor to the Arduino pins as specified in the ArduimoSerial file

