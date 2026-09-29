# Program 2 — Binary Classification Model
# 
# Build:
# 
# 3 inputs
 # ↓
# 8 neurons
 # ↓
# ReLU
 # ↓
# 4 neurons
 # ↓
# ReLU
 # ↓
# 1 output
# 
# Use:
# 
# nn.Module
# nn.Linear
# nn.ReLU
# 
# Print:
# 
# architecture
# parameter names
# parameter shapes
# total parameters

import torch
import torch.nn as nn

class BinaryClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.layer1=nn.Linear(3,8)
        self.relu1=nn.ReLU()

        self.layer2=nn.Linear(8,4)
        self.relu2=nn.ReLU()

        self.output=nn.Linear(4,1)

    def forward(self,x):
        x=self.layer1(x)
        x=self.relu1(x)

        x=self.layer2(x)
        x=self.relu2(x)

        x=self.output(x)

        return x 


model=BinaryClassifier()

# Print Architecture 
print("----------Architecture----------")
print(model)

# Print Parameter Names and  Parameter Shapes

print("\n-----------Parameter Names & Shapes----------")

for name,parameter in model.named_parameters():
    print(name,parameter.shape)


# Calculate Total Parameters

total_parameters=sum(
    parameter.numel()
    for parameter in model.parameters()
)

print("\nTotal No.of Parameters Are :",total_parameters)