import sys
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/skin_model.h5")

image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Image not found: {image_path}")
    sys.exit(1)

img = cv2.resize(img, (128, 128))
img = img / 255.0
img = np.expand_dims(img, axis=0)

pred = model.predict(img)
score = float(pred[0][0])

if score > 0.5:
    print(f"Cancer ({score:.4f})")
else:
    print(f"Non-Cancer ({score:.4f})")