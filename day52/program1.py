# Program 1 — Create and Inspect Tensors
# tensor_basics.py


import torch 

scalar=torch.tensor(5)

vector=torch.tensor([1,2,3])

matrix=torch.tensor([
    [1,2],
    [3,4]
])

print("Scalar :\n",scalar)
print("Shape of Scalar :",scalar.shape)

print("\nVector \n",vector)
print("Shape of Vector :",vector.shape)

print("\nMatrix :\n",matrix)
print("Shape of Matrix :",matrix.shape)