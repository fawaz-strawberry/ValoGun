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

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

EPOCHS = 10
BATCH_SIZE = 4
LEARNING_RATE = 0.01
NUM_CHANNELS = 1
HEIGHT = 64
WIDTH = 64

INPUT_SIZE  = (64, 64)
OUTPUT_SIZE = 2

n_samples = 1024

CLASSES = ['crouch', 'stand', 'jump']

MODEL_PATH = "C:/Users/fawaz/Documents/GitHub/ValoGun/ml_models/"

#x = (torch.randn((BATCH_SIZE, NUM_CHANNELS, HEIGHT, WIDTH))).to(device)


# LOAD DATA
transforms = transforms.Compose(
    [   transforms.Grayscale(num_output_channels=1),
        transforms.Resize((HEIGHT, WIDTH)),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.5 for _ in range(NUM_CHANNELS)], [0.5 for _ in range(NUM_CHANNELS)])
    ]
)

train_dataset = datasets.ImageFolder(root="C:/Users/fawaz/Videos/ValoRedScreen_2/train", transform=transforms)
test_dataset = datasets.ImageFolder(root="C:/Users/fawaz/Videos/ValoRedScreen_2/test", transform=transforms)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=True)


# CREATE MODEL
model = FeetCNN().to(device)

# LOSS AND OPTIMIZER
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)



def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        i = 0
        for x, y in loader:
            i += 1
            if(i > n_samples):
                break
            x = x.to(device)
            y = y.to(device)
            
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
            #print(num_samples)

        print("Accuracy: " + str((float(num_correct) / num_samples) * 100) + "%")
        return (float(num_correct) / num_samples)

check_accuracy(test_loader, model)

# TRAIN NETWORK


print("Starting to train")

train_time = str(int(time.time()))
max_acc = 0
for epoch in range(EPOCHS):
    for batch_idx, (data, targets) in enumerate(train_loader):
        if(batch_idx > n_samples):
            break
        data = data.to(device)
        targets = targets.to(device)

        #forward
        scores = model(data)
        loss = criterion(scores, targets)

        #backward
        optimizer.zero_grad()
        loss.backward()

        #gradient descent or adam step
        optimizer.step()
    print("Epoch: " + str(epoch))
    acc2 = check_accuracy(train_loader, model)
    acc = check_accuracy(test_loader, model)
    if(acc > max_acc):
        max_acc = acc
        torch.save(model.state_dict(), MODEL_PATH + "model_" + train_time + ".pth")
        #Save model

# CHECK ACCURACY

