import os
from PIL import Image
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    
    def __init__(self, root_dir, transform=None):
        self.samples = []
        self.transform = transform
        
        self.label_map = {}
        
        labels = sorted(os.listdir(root_dir))
        for i, label in enumerate(labels):
            self.label_map[label] = i
        
        for label in labels:
            for file in os.listdir(os.path.join(root_dir, label)):
                self.samples.append((
                    os.path.join(root_dir, label, file),
                    self.label_map[label]
                ))
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        path, label = self.samples[idx]
        img = Image.open(path).convert("RGB")
        
        if self.transform:
            img = self.transform(img)
        
        return img, label