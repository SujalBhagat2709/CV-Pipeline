from dataset_dataloader import CustomDataset
from data_augmentation import get_augmentation
from torch.utils.data import DataLoader
import torch

def get_loader():
    
    transform = get_augmentation()
    
    dataset = CustomDataset("data/train", transform)
    
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    
    return loader