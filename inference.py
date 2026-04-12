import torch
from PIL import Image
from torchvision import transforms

def predict(model, image_path, device):
    
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    
    img = Image.open(image_path).convert("RGB")
    
    img = transform(img).unsqueeze(0).to(device)
    
    model.eval()
    
    with torch.no_grad():
        output = model(img)
        pred = output.argmax(dim=1)
    
    return pred.item()