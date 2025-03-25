import time
import cv2

webcam = cv2.VideoCapture(0) # Select Camera
time.sleep(1)

while True:
    check, frame = webcam.read()
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'): # Command to break
        break

webcam.release()