import cv2, time, math
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

webcam = cv2.VideoCapture(0) # Select Camera
status_webcam = [0, 0]
last_detected_frame = None

time.sleep(1)
while True:
    status = 0
    check, frame = webcam.read()
    detections = model(frame, stream=True)

    for r in detections:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (204, 175, 255), 2)

            confidence = math.ceil((box.conf[0] * 100)) / 100
            # print("Confidence --->", confidence)

            cls = int(box.cls[0])
            # print("Class name -->", classNames[cls])

            if confidence > 0.8:
                status = 1
                last_detected_frame = frame.copy()

            status_webcam.append(status)
            status_webcam = status_webcam[-2:]
            print(status_webcam)

            if status_webcam == [1, 0] and last_detected_frame is not None:
                if time.time() - last_detected_frame.any() > 2:
                    cv2.imwrite("image.png", last_detected_frame)
                    last_detected_frame = time.time()

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_DUPLEX
            fontScale = 1
            color = (204, 175, 255)
            thickness = 2

            cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()