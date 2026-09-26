import torch
import torch.nn as nn

layer=nn.Linear(3,4)

print(layer)

print("Weight Shape :",layer.weight.shape)
print("Bias Shape   :",layer.bias.shape)