from ultralytics import YOLO

model=YOLO("path/your/model")

model.predict(source="0", show=True)