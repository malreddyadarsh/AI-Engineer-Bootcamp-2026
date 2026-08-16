# Linear Algebra Data Processor
# 
# Build a small NumPy application that accepts two vectors/matrices and performs:
# 
# Addition
# Subtraction
# Dot product
# Matrix multiplication
# Transpose
# Norm
# Euclidean distance
# 
# Then display a simple explanation for each result.

import numpy as np

print("1. For vectors ")
print("2. For Matrices ")

ch=int(input("Enter your Choice :"))
if ch==1 :
    vec1=np.array([1,2,3])
    vec2=np.array([4,5,6])

    # Addition 
    print("\n Addition :\n",vec1+vec2)

    # Subtraction
    print("\nSubtraction :\n",vec2-vec1)

    # dot Product
    print("\nDot Product :\n",np.dot(vec1,vec2))

    # Norm
    norm1=np.linalg.norm(vec1)
    norm2=np.linalg.norm(vec2)
    print("\nNorm 1 :",norm1)
    print("\nNorm 2 :",norm2)

    # Euclidean distance
    dist=np.linalg.norm(vec2-vec1)
    print("Distance B/W two vectors :",dist)
elif ch==2:
    a=np.array([
        [23,45],
        [56,74]
    ])

    b=np.array([
        [34,54],
        [24,42]
    ])

    # Addition
    print("\nAddition :\n",a+b)

    # Subtraction
    print("\nSubtraction :\n",a-b)

    # Matrix multiplication
    print("\nMatrix multiplication :\n",a@b)

    # Transpose
    print("\nTranspose :\n",np.transpose(a))

else:
    print("Invalid Option.")