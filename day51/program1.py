# Program 1 — Implement a Single Neuron with NumPy

import numpy as np 

x=np.array([2.0,3.0])

w=np.array([0.5,0.2])

b=0.1

z=np.dot(w,x)+b

print(f"Weighted Sum is :{z:.2f}")