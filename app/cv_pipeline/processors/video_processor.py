# app/cv_pipeline/processors/video_processor.py
import cv2
import json

class VideoProcessor:
    def __init__(self, video_path, pipeline, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.pipeline = pipeline
        self.output_path = output_path

        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))

        self.out = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            30,
            (self.width, self.height)
        )

        self.json_file = open("output/output.json", "w")

    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            result, _ = self.pipeline.process_frame(frame)

            self.json_file.write(json.dumps(result) + "\n")
            print(result)

            self.out.write(frame)

        self.cap.release()
        self.out.release()
        self.json_file.close()