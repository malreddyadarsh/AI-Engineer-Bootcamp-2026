import torch 

a=torch.zeros(2,4)

b=torch.ones(2,3)

c=torch.rand(3,2)

d=torch.randn(3,2)

e=torch.arange(0,10)

print("Zeros :\n",a)

print("\nOnes :\n",b)

print("\nRandom :\n",c)

print("\nRandom normal distribution :\n",d)

print("\nRange :\n",e)