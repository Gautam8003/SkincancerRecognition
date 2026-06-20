# SkinCancerRecognition

A simple skin cancer classification project using TensorFlow, Flask, and OpenCV.

## Project structure

- `prepare_dataset.py` - split the HAM10000 dataset into `dataset/train/benign` and `dataset/train/malignant`
- `train.py` - train a binary CNN and save `models/skin_model.h5`
- `predict.py` - run a command-line image prediction
- `app.py` - Flask web app for image upload and prediction
- `templates/index.html` - web UI for user uploads

## Setup

1. Create and activate a Python environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the project

1. Prepare the dataset:

```powershell
python prepare_dataset.py
```

2. Train the model:

```powershell
python train.py
```

3. Start the Flask app:

```powershell
python app.py
```

4. Open the app in your browser:

```text
http://127.0.0.1:5000
```

## Command-line prediction

Use a local image file name or path:

```powershell
python predict.py path\to\image.jpg
```

If no path is provided, the script will try to load `test.jpg` from the project root.

## Notes

- The app saves uploaded files to `static/uploads/`.
- If you want to keep the trained model in Keras native format, change `model.save("models/skin_model.h5")` to `model.save("models/skin_model.keras")`.
