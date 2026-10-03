# Program 2 — Calculate Metrics Manually
# 
# Given:
# 
# actual = torch.tensor([
    # [10.0],
    # [20.0],
    # [30.0]
# ])
# 
# prediction = torch.tensor([
    # [12.0],
    # [18.0],
    # [27.0]
# ])
# 
# Calculate manually with PyTorch:
# 
# MAE
# MSE
# RMSE
# 
# Then verify using scikit-learn.

import torch
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error

actual=torch.tensor([
    [10.0],
    [20.0],
    [30.0]
])

predicted=torch.tensor([
    [12.0],
    [18.0],
    [27.0]
])

# Calculate Errors 

errors=actual - predicted

print("Errors :")
print(errors)

mae=torch.mean(torch.abs(errors))

print("MAE :",mae.item())

mse=torch.mean(errors ** 2)

print("MSE :",mse.item())

rmse=torch.sqrt(mse)

print("RMSE :",rmse.item())

# Convert tensors to 1D Numpy Arrays

actual_np=actual.numpy().flatten()
predicted_np=predicted.numpy().flatten()

sk_mae=mean_absolute_error(actual_np,predicted_np)

sk_mse=mean_squared_error(actual_np,predicted_np)

sk_rmse=mse ** 0.5

print("\nUSing SKLEARN")

print("Sklearn MAE :",sk_mae)
print("Sklearn MSE :",sk_mse)
print("Sklearn MAE :",sk_rmse)