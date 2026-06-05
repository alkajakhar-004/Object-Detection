import cv2
from ultralytics import YOLO

# apna trained model load karo
model = YOLO(r"C:\Users\Admin\runs\detect\train\weights\best.pt")  # yahan exact path use karo

cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # prediction + draw boxes
    results = model(frame, conf=0.5)   # confidence adjust kar sakta hai
    annotated = results[0].plot()      # YOLOv8 ka built-in drawing [web:81]

    cv2.imshow("YOLOv8 Live", annotated)

    if cv2.waitKey(1) & 0xFF == 27:    # ESC dabao to exit
        break

cap.release()
cv2.destroyAllWindows()