from flask import Flask, render_template, request
from tensorflow.keras.models import load_model


from werkzeug.utils import secure_filename
import cv2
import numpy as np
import os

app = Flask(__name__)


model = load_model("models/skin_model.h5")

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("image")
    if file is None or file.filename == "":
        return render_template("index.html", error="Please upload an image file.")

    filename = secure_filename(file.filename)
    if filename == "":
        return render_template("index.html", error="Invalid file name.")

    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    img = cv2.imread(path)
    if img is None:
        return render_template("index.html", error="Unable to read uploaded image.")

    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    score = float(pred[0][0])
    
    # Class 0 is Malignant (Cancer), Class 1 is Benign (Non-Cancer)
    if score > 0.5:
        result = "Non-Cancer"
        confidence = score * 100
    else:
        result = "Cancer"
        confidence = (1.0 - score) * 100

    # Determine confidence level and clinical interpretation
    if confidence >= 80.0:
        confidence_level = "High"
        if result == "Non-Cancer":
            interpretation = "The lesion appears likely to be non-cancerous."
        else:
            interpretation = "The lesion appears likely to be cancerous. Professional medical consultation is highly recommended."
    elif confidence >= 60.0:
        confidence_level = "Medium"
        if result == "Non-Cancer":
            interpretation = "The lesion is predicted as non-cancerous, but further examination may be advisable."
        else:
            interpretation = "The lesion is predicted as cancerous, and further examination is advisable."
    else:
        confidence_level = "Low"
        interpretation = "The model is uncertain. Please consult a dermatologist."

    return render_template(
        "index.html",
        prediction=result,
        confidence=f"{confidence:.2f}",
        confidence_level=confidence_level,
        interpretation=interpretation,
        image=path
    )


if __name__ == "__main__":
    app.run(debug=True)