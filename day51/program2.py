# Program 2 — Add ReLU

import numpy as np

x=np.array([2.0,3.0])

w=np.array([0.5,0.2])

b=-2.0

z=np.dot(w,x)+b

a=max(0,z)

print(f"Weighted Sum :{z:.2f}")

print(f"ReLU Output is :{a}")