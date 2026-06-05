from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt")  # pre-trained model
    model.train(
        data="data/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        workers=2
    )

if __name__ == "__main__":
    train_model()
