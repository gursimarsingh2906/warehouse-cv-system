import cv2
import os
from app.cv_pipeline.pipeline.box_pipeline import BoxPipeline
from app.cv_pipeline.processors.video_processor import VideoProcessor

# -----------------------------
# CONFIG
# -----------------------------
VIDEO_PATH = r"C:\Users\hp\Desktop\warehousecvsystem\app\boxes detection.mp4"
MODEL_PATH = r"C:\Users\hp\Desktop\warehousecvsystem\app\models\best.pt"
OUTPUT_VIDEO = r"C:\Users\hp\Desktop\warehousecvsystem\ouput.mp4"

# -----------------------------
# MAIN RUNNER
# -----------------------------
def main():
    # create output folder
    os.makedirs("output", exist_ok=True)

    # read video to get dimensions
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("❌ Error: Cannot open video")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))
    cap.release()

    # initialize pipeline
    pipeline = BoxPipeline(
        model_path=MODEL_PATH,
        width=width,
        height=height,
        camera_id="CAM_LOCAL"
    )

    # initialize processor
    processor = VideoProcessor(
        video_path=VIDEO_PATH,
        pipeline=pipeline,
        output_path=OUTPUT_VIDEO
    )

    # run pipeline
    processor.run()

    print("✅ Processing completed")
    print(f"🎥 Video saved at: {OUTPUT_VIDEO}")
    print(f"📄 JSON saved at: output/output.json")


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()