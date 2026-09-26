import torch

x=torch.tensor(2.0,requires_grad=True)

y=x**2
z=3*y

z.backward()

print("x :",x)

print("y :",y)
print("z :",z)
print("Gradient :",x.grad)