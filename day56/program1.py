# Day 56 Practice Set
# Program 1 — Basic Regression
# 
# Create:
# 
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# 
# Train:
# 
# nn.Linear(1,1)
# MSELoss
# Adam
# 
# Predict:
# 
# x = 7
# 
# Expected result should be close to:
# 
# 14

import torch
import torch.nn as nn

# Training data
x = torch.tensor([[1.0],
                  [2.0],
                  [3.0],
                  [4.0],
                  [5.0]])

y = torch.tensor([[2.0],
                  [4.0],
                  [6.0],
                  [8.0],
                  [10.0]])

# Model
model = nn.Linear(1, 1)

# Loss function
loss_fn = nn.MSELoss()

# Optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training
for epoch in range(1000):

    # Forward pass
    predictions = model(x)

    # Calculate loss
    loss = loss_fn(predictions, y)

    # Clear old gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch: {epoch}, Loss: {loss.item():.6f}")

# Prediction
test_x = torch.tensor([[7.0]])

prediction = model(test_x)

print("\nPrediction for x = 7:", prediction.item())

# Learned parameters
print("Learned weight:", model.weight.item())
print("Learned bias:", model.bias.item())