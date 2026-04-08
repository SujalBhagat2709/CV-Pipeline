import torch.nn as nn
from torchvision import models

def build_model(num_classes=2):
    
    model = models.resnet18(pretrained=True)
    
    for param in model.parameters():
        param.requires_grad = False
    
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    
    return model


model = build_model()

print("Model built")
