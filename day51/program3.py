import numpy as np

x = np.array([[2.0],
              [3.0],
              [1.0]])

W1 = np.array([
    [0.5, 0.2, 0.1],
    [0.4, 0.3, 0.2],
    [0.1, 0.7, 0.5],
    [0.6, 0.2, 0.4]
])

b1 = np.zeros((4, 1))

z1 = W1 @ x + b1

a1 = np.maximum(0, z1)

print("Hidden layer output:")
print(a1)

W2 = np.array([
    [0.3, 0.5, 0.2, 0.4]
])

b2 = np.array([[0.1]])

z2 = W2 @ a1 + b2

print("Output:")
print(z2)