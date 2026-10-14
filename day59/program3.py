# Task 3 — LayerNorm
# Normalize the same tensor with LayerNorm(3) and explain how each sample is handled.

import torch
import torch.nn as nn

layer_norm=nn.LayerNorm(3)

x=torch.tensor([
    [10.0,100.0,1000],
    [20.0,200.0,2000.0],
    [30.0,300.0,3000.0]
])

output=layer_norm(x)

print("\nInput :")
print(x)

print("\nNormalized Data :")
print(output)