# Program 5 — Complete Training + Validation

import torch 
import torch.nn as nn
from torch.utils.data import DataLoader,random_split,TensorDataset

# Dataset

x=torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0],
    [7.0],
    [8.0],
    [9.0],
    [10.0]
])

y=torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0],
    [12.0],
    [14.0],
    [16.0],
    [18.0],
    [20.0]    
])

dataset=TensorDataset(x,y)

# Train/Validation Split of Dataset

train_size=int(0.8*len(dataset))

validation_size=len(dataset)-train_size

train_dataset,validation_dataset=random_split(
    dataset,
    [train_size,validation_size]
)

# DataLoader
train_loader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

validation_loader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=False
)

# Model Name 
model=nn.Linear(1,1)

# Loss Function
loss_function=nn.MSELoss()

# Optimizer
optimizer=torch.optim.SGD(
    model.parameters(),
    lr=.01
)

epochs=100

for epoch in range(epochs):

    # Training Dataset

    model.train()
    total_train_loss=0

    for batch_x,batch_y in train_loader:

        optimizer.zero_grad()

        prediction=model(batch_x)

        loss=loss_function(prediction,batch_y)

        loss.backward()

        optimizer.step()

        total_train_loss+=loss.item()

    # Validation

    model.eval()
    
    total_validation_loss=0

    for batch_x,batch_y in validation_loader:

        with torch.no_grad():
            prediction=model(batch_x)

            loss=loss_function(prediction,batch_y)

            total_validation_loss+=loss.item()


    if epoch % 10 == 0:

        average_train_loss = (total_train_loss / len(train_loader))
        average_validation_loss = (total_validation_loss / len(validation_loader))

        print(
            f"Epoch           :{epoch}",
            f"\nTrain Loss      :{average_train_loss:.6f}",
            f"\nValidation Loss :{average_validation_loss:.6f}"
        )

        print("--------------------------------------------")