# Object Detection and Email Sending

This project uses **YOLO** to detect objects in images captured by the webcam and automatically sends the detected images via email.

## 🚀 Technologies Used
- Python 3.10 (Conda)
- OpenCV
- YOLO (You Only Look Once)
- Threading
- Queue
- Glob

## 📌 Features
- Captures images from the webcam.
- Detects objects using **YOLO**.
- Saves images when objects are detected.
- Sends captured images via email.
- Manages the email sending queue using **threads**.
- Deletes old images to optimize storage.

## 📂 Project Structure
```
/
├── images/              # Directory where detected images are stored
├── utils/
│   ├── send_mail.py         # Script for sending emails
│   ├── get_webcam_info.py   # Script to identify your webcam
├── face_detection.py    # Script for facial detection without email sending
├── main.py              # Main script of the project
├── yolo11n.pt           # Pre-trained YOLO model
└── README.md            # Project documentation
```

## 🛠️ How to Use
1. **Create a Conda environment and install the dependencies:**
   ```bash
   conda create -n obj_detection python=3.10 -y
   conda activate obj_detection
   pip install opencv-python ultralytics
   ```
2. **Run the main script:**
   ```bash
   python main.py
   ```
3. **Press 'q' to exit the program.**

## 📧 Email Configuration
To enable the automatic sending of images, edit `utils/send_mail.py` with your SMTP credentials.

## ⚠️ Requirements
- Python 3.10 (Conda)
- Webcam connected
