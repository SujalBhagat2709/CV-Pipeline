import torch

def validate(model, loader, device):
    
    model.eval()
    
    correct = 0
    total = 0
    
    with torch.no_grad():
        for images, labels in loader:
            
            images = images.to(device)
            labels = labels.to(device)
            
            outputs = model(images)
            
            preds = outputs.argmax(dim=1)
            
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    
    accuracy = correct / total
    
    print("Validation Accuracy:", accuracy)