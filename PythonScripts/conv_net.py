import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

#((W-F+2*P )/S)+1

class FeetCNN(torch.nn.Module):
    def __init__(self):
        super(FeetCNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, kernel_size=5)#Output = ((64-3+2*1)/1) + 1 = 64
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)#Output = ((64-2+2*0)/2) + 1 = 32
        self.conv2 = torch.nn.Conv2d(6, 16, 5)
        self.fc1 = torch.nn.Linear(16*13*13, 120)
        self.fc2 = torch.nn.Linear(120, 84)
        self.fc3 = torch.nn.Linear(84, 3)

    def forward(self, x):
        #Layer 1
        x = F.leaky_relu(self.conv1(x))
        x = self.pool(x)
        #layer 2
        x = F.leaky_relu(self.conv2(x))
        x = self.pool(x)
        #Fully Connected 3
        x = x.view(-1, 16*13*13)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = (self.fc3(x))

        return(x)
