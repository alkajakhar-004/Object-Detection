import os

train_path = "D:/Object-Detection-Project/data/coco128/images/train"
val_path   = "D:/Object-Detection-Project/data/coco128/images/val"

print("Train folder exists:", os.path.exists(train_path))
print("Val folder exists:", os.path.exists(val_path))

print("Train folder contents:", os.listdir(train_path) if os.path.exists(train_path) else "Not found")
print("Val folder contents:", os.listdir(val_path) if os.path.exists(val_path) else "Not found")
