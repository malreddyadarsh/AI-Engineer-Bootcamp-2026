import torch

x=torch.tensor([
    [1,2],
    [3,4]
],dtype=torch.float32)

y=torch.tensor([
    [5,6],
    [7,8]
],dtype=torch.float32)

print("Addition:")
print(x+y)

print("\nSubstraction :")
print(x-y)

print("\nElement-Wise Multiplication :")
print(x*y)

print("\nDivision :")
print(x/y)

print("\nMatrix Multiplication :")
print(x@y)

print("\nMean of x :")
print(x.mean())

print("\nSum of x :")
print(x.sum())

print("\nMax of x :")
print(x.max())

print("\nMin of x :")
print(x.min())