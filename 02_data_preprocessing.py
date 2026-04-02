import cv2

def preprocess_image(path, size=224):
    
    img = cv2.imread(path)
    
    img = cv2.resize(img, (size, size))
    
    img = img / 255.0
    
    return img


sample_path = "data/train/class1/img1.jpg"

img = preprocess_image(sample_path)

print("Preprocessing done:", img.shape)