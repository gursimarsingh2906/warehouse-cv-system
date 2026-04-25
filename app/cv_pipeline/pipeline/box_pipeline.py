# app/cv_pipeline/pipeline/box_pipeline.py
import supervision as sv
from app.cv_pipeline.detectors.yolo_detector import YOLODetector
from app.cv_pipeline.trackers.tracker import ObjectTracker
from app.cv_pipeline.counters.line_counter import LineCounter
from app.cv_pipeline.events.event import Event

class BoxPipeline:
    def __init__(self, model_path, width, height, camera_id):
        self.detector = YOLODetector(model_path)
        self.tracker = ObjectTracker()
        self.counter = LineCounter(width, height)
        self.camera_id = camera_id

    def process_frame(self, frame):
        results = self.detector.detect(frame)

        detections = sv.Detections.from_ultralytics(results)
        detections = self.tracker.update(detections)

        count = self.counter.count(detections)

        event = Event(self.camera_id, count)

        return event.to_dict(), detections