import cv2 
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data.sampler import BatchSampler
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
from torchvision.transforms.transforms import Grayscale
from conv_net import FeetCNN
import os
import time
import pyautogui
# Imports PIL module 
from PIL import Image
  


url = 'http://192.168.0.137:4747/video'
cap = cv2.VideoCapture(url)

NUM_CHANNELS = 1
HEIGHT = 64
WIDTH = 64

CLASSES = ['crouch', 'jump', 'stand']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = FeetCNN().to(device)
model.load_state_dict(torch.load("C:/Users/fawaz/Documents/GitHub/ValoGun/ml_models/model_1628439678.pth"))
model.eval()


# LOAD DATA
transforms = transforms.Compose(
    [   transforms.Grayscale(num_output_channels=1),
        transforms.Resize((HEIGHT, WIDTH)),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.5 for _ in range(NUM_CHANNELS)], [0.5 for _ in range(NUM_CHANNELS)])
    ]
)

while(True):
    ret, frame = cap.read()
    q = cv2.waitKey(1)
    if frame is not None:
        resized = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA)
        cv2.imwrite('frame.png',resized)
        cv2.imshow('frame',frame)
        if q == ord("q"):
            break

        with torch.no_grad():
            # open method used to open different extension image file
            im = Image.open(r"frame.png")
            final_im = transforms(im)
            final_im = final_im.unsqueeze(1)
            final_im = final_im.to(device)
            output = model(final_im)
            print(CLASSES[np.argmax(output.cpu().numpy()[0])])
            
            my_event = CLASSES[np.argmax(output.cpu().numpy()[0])]
            if(my_event == "stand"):
                pyautogui.keyUp("shift")
            if(my_event == "jump"):
                pyautogui.press("space")                
            if(my_event == "crouch"):
                pyautogui.keyDown("shift")
            pass                                               
cv2.destroyAllWindows()