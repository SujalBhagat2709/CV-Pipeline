import os
import zipfile
import subprocess

DATA_DIR = "data"
DATASET_NAME = "dogs-vs-cats"

def download_dataset():
    
    if os.path.exists(DATA_DIR):
        print("Dataset already exists")
        return
    
    os.makedirs(DATA_DIR, exist_ok=True)
    
    print("Downloading dataset...")
    
    subprocess.run([
        "kaggle", "competitions", "download",
        "-c", "dogs-vs-cats"
    ])
    
    zip_path = "dogs-vs-cats.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(DATA_DIR)
    
    print("Dataset downloaded & extracted")

def organize_data():
    
    print("Organizing dataset...")
    
    train_dir = os.path.join(DATA_DIR, "train")
    
    cats_dir = os.path.join(train_dir, "cats")
    dogs_dir = os.path.join(train_dir, "dogs")
    
    # ✅ If already organized → skip
    if os.path.exists(cats_dir) and os.path.exists(dogs_dir):
        print("Dataset already organized")
        return
    
    os.makedirs(cats_dir, exist_ok=True)
    os.makedirs(dogs_dir, exist_ok=True)
    
    for file in os.listdir(train_dir):
        
        file_path = os.path.join(train_dir, file)
        
        # ❗ Skip directories (IMPORTANT FIX)
        if os.path.isdir(file_path):
            continue
        
        if "cat" in file:
            os.rename(file_path, os.path.join(cats_dir, file))
        elif "dog" in file:
            os.rename(file_path, os.path.join(dogs_dir, file))
    
    print("Data organized successfully")

if __name__ == "__main__":
    download_dataset()
    organize_data()