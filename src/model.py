import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class LinearModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(FeedForward, self).__init__()
        self.fc1 = nn.Linear(self.input_size, self.hidden_size)
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, x):
        return self.fc1(x)