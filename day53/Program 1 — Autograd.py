import torch

x=torch.tensor(3.0,requires_grad=True)

y = (x**2) + (2*x) + 1

y.backward()

print("Gradient of x :",x.grad)