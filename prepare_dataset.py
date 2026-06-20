import pandas as pd 
import os 
import shutil 

metadata = pd.read_csv(r"D:\Gautam\Projects\SkinCancerRecognition\dataset\Hamset\HAM10000_metadata.csv")

os.makedirs("dataset/train/benign", exist_ok=True)
os.makedirs("dataset/train/malignant", exist_ok=True)

for _, row in metadata.iterrows():
    image = row["image_id"] + ".jpg"
    label = row["dx"]
    source = os.path.join("dataset", "HamsetImages", image)

    if os.path.exists(source):
        if label in ["nv", "bkl"]:
            shutil.copy(source, "dataset/train/benign")

        if label in ["mel", "bcc"]:
            shutil.copy(source, "dataset/train/malignant")

print("Dataset Prepared")

