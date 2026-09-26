# Program 1 — First Training Loop

import torch 
import torch.nn as nn

# Training Data

x=torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y=torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0]
])

# Model
model=nn.Linear(1,1)

# Loss Function
loss_function=nn.MSELoss()

# Optimizer
optimizer=torch.optim.SGD(model.parameters(),lr=0.01)

# Training

for epoch in range(1000):

    # Removing Gradients
    optimizer.zero_grad()

    # Forward Pass
    prediction=model(x)

    # Calaculate loss
    loss=loss_function(prediction,y)

    #Calculate Gradients
    loss.backward()

    #Update Parameters 
    optimizer.step()

    if epoch % 100 ==0 :
        print(
            f"Epoch :{epoch}",
            f"Loss :{loss.item():.6f}"
        )

test=torch.tensor([[6.0]])

with torch.no_grad():
    prediction=model(test)

print("Prediction for 6 is :",prediction.item())

print("Weight:", model.weight.item())
print("Bias:", model.bias.item())

print("Weight gradient:")
print(model.weight.grad)

print("Bias gradient:")
print(model.bias.grad)