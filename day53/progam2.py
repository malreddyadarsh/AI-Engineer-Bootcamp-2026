import torch
import torch.nn as nn

class StudentModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1=nn.Linear(3,4)
        self.relu=nn.ReLU()
        self.output=nn.Linear(4,1)

    def forward(self,x):

        x=self.layer1(x)

        x=self.relu(x)

        x=self.output(x)

        return x

model=StudentModel()

print(model)
