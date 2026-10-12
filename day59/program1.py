# Task 1 — StandardScaler
# Standardize a numerical array and inspect its mean and standard deviation.

import numpy as np
from sklearn.preprocessing import StandardScaler

# Step 1: Create a numerical array
data = np.array([[10], [20], [30], [40], [50]])

# Original Data
print("Original Data :")
print(data)

scaler=StandardScaler()

scaled_data=scaler.fit_transform(data)

print("\nStandardized Data :")
print(scaled_data)

print("\nMean of Scaled Data :")
print(f"{scaled_data.mean():.2f}")

print("\nStandard Deviation of Scaled Data is :")
print(f"{scaled_data.std():.2f}")