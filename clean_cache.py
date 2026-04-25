import os
import shutil

for root, dirs, files in os.walk("."):
    for d in dirs:
        if d == "__pycache__":
            path = os.path.join(root, d)
            shutil.rmtree(path, ignore_errors=True)
            print(f"Deleted: {path}")