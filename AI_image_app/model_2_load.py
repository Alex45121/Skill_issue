import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.init as init
import tkinter as tk
import os
from tkinter import filedialog, Label, Button

# ----- Model definition (same as used for model_2) -----
class StyleNet(nn.Module):
    def __init__(self):
        super(StyleNet, self).__init__()

        # Feature extractor (CNN)
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)

        # Fully connected layers (MLP)
        self.fc1 = nn.Linear(32 * 64 * 64, 128)
        self.fc2 = nn.Linear(128, 4)  # 4 outputs: style_look, prop_style, color_grading, scene_mood

        init.xavier_uniform_(self.conv1.weight)
        init.xavier_uniform_(self.conv2.weight)
        init.xavier_uniform_(self.fc1.weight)
        init.xavier_uniform_(self.fc2.weight)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        x = x.view(x.size(0), -1)  # Flatten

        x = F.relu(self.fc1(x))
        x = F.dropout(x, p=0.5, training=self.training) # Dropout added
        x = self.fc2(x)  # Final output

        return x

# ----- Load model -----
model_2 = StyleNet()

device_use = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model_path = os.path.join(os.path.dirname(__file__), "model_2_weights.pth")

model_2.load_state_dict(torch.load(model_path, map_location=device_use))

model_2.eval()

# ----- Image Transform -----
transform_pipeline = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# ----- GUI -----
def predict_image(img):
    
    img_t = transform_pipeline(img).unsqueeze(0).to(device_use)
    
    with torch.no_grad():
        prediction = model_2(img_t)
        prediction = torch.clamp(prediction, 0, 10)  # Optional clamp

    return prediction.cpu()
       

