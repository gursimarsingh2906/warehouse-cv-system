# app/cv_pipeline/counters/line_counter.py
import supervision as sv

class LineCounter:
    def __init__(self, width, height):
        x = width // 2
        self.line = sv.LineZone(
            start=sv.Point(x=x, y=0),
            end=sv.Point(x=x, y=height)
        )

    def count(self, detections):
        self.line.trigger(detections)
        return int(self.line.in_count)