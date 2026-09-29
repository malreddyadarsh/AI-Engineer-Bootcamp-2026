# Program 1 — Sigmoid
# 
# Create several logits:
# 
# [-5, -2, 0, 2, 5]
# 
# Apply:
# 
# torch.sigmoid()
# 
# Print the probabilities.
# 
# Understand why:
# 
# negative → probability < 0.5
# zero     → probability = 0.5
# positive → probability > 0.5

import torch 

x=torch.tensor([
    [-5],
    [-2],
    [0],
    [2],
    [5]
])

probabilities=torch.sigmoid(x)

print("Probabilities :",probabilities)