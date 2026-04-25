# app/main.py
from fastapi import FastAPI
from app.cv_pipeline.pipeline.box_pipeline import BoxPipeline
from app.cv_pipeline.processors.video_processor import VideoProcessor
import cv2

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Warehouse CV System Running"}

@app.post("/run")
def run_pipeline():
    video_path = r"C:\Users\hp\Desktop\warehousecvsystem\app\boxes detection.mp4"

    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(3))
    height = int(cap.get(4))
    cap.release()

    pipeline = BoxPipeline(
        model_path=r"C:\Users\hp\Desktop\warehousecvsystem\app\models\best.pt",
        width=width,
        height=height,
        camera_id="CAM_01"
    )

    processor = VideoProcessor(video_path, pipeline, "output/output.mp4")
    processor.run()

    return {"status": "processing completed"}