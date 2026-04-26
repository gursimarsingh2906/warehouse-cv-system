# app/cv_pipeline/events/event.py
import datetime

class Event:
    def __init__(self, camera_id, count):
        self.camera_id = camera_id
        self.count = count
        self.timestamp = datetime.datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "camera_id": self.camera_id,
            "box_count": self.count,
            "timestamp": self.timestamp
        }