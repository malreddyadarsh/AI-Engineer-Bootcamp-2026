# Program 4 — Train/Validation Split

import torch
from torch.utils.data import random_split,DataLoader,TensorDataset

x=torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y=torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0],
    [12.0]
])

dataset=TensorDataset(x,y)

train_size=int(0.8*len(dataset))
validatation_size=len(dataset)-train_size

train_dataset,validation_dataset=random_split(
    dataset,
    [train_size,validatation_size]
)

train_loader=DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

validation_loader=DataLoader(
    validation_dataset,
    batch_size=32,
    shuffle=False
)
