# Task 2 — BatchNorm1d
# Use a [4, 3] tensor and explain why the layer is BatchNorm1d(3).


import torch
import torch.nn as nn

batch_norm=nn.BatchNorm1d(3)

x=torch.tensor([
    [10.0,100.0,1000.0],
    [20.0,200.0,2000.0],
    [30.0,300.0,3000.0],
    [40.0,400.0,4000.0]
])

output=batch_norm(x)

print("Input :")
print(x)

print("Normalized Data :")
print(output)