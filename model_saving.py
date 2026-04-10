import torch

def save_model(model, path="models/model.pth"):
    
    torch.save(model.state_dict(), path)
    
    print("Model saved at", path)