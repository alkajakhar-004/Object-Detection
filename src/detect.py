import cv2
from ultralytics import YOLO
import time

model = YOLO("models/best.pt")    # trained model

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    start = time.time()
    results = model(frame)
    end = time.time()

    fps = 1 / (end - start)

    annotated_frame = results[0].plot()

    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
