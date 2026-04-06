from torchvision import transforms

def get_augmentation():
    
    return transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2),
        transforms.ToTensor()
    ])


aug = get_augmentation()

print("Augmentation pipeline ready")
