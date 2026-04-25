# app/cv_pipeline/detectors/yolo_detector.py

print("YOLO DETECTOR FILE LOADED")
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        return self.model(frame)[0]