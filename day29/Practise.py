# # Program 1 — Vector Operations
# # 
# # Create two vectors and calculate:
# # 
# # Addition
# # Subtraction
# # Scalar multiplication
# # Dot product
# # 
# # Use NumPy.
# 
# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# 
# # Addition
# print("\nAddition :",a+b)
# 
# # Subtraction
# print("\nSubtraction :",a-b)
# 
# # Scalar multiplication
# print("\nScalar multiplication :",2*a)
# 
# # Dot product
# res=np.dot(a,b)
# print("\nDot product :",res)

# # Program 2 — Matrix Operations
# # 
# # Create two compatible matrices and perform:
# # 
# # Addition
# # Subtraction
# # Element-wise multiplication
# # Matrix multiplication
# # 
# # Then explain the difference between * and @.

# import numpy as np

# a=np.array([
    # [1,2,3],
    # [4,5,6]
# ])
# b=np.array([
    # [4,5,6],
    # [7,8,9]
# ])

# # Addition
# print("\nAddition :\n",a+b)

# # Subtraction
# print("\nSubtraction :\n",b-a)

# # Element-wise multiplication
# print("\nElement-wise multiplication :\n",a*b)

# c=np.transpose(b)

# # Matrix multiplication
# print("\nMatrix multiplication :\n",a@c)


# # Program 3 — Matrix Shape & Transpose
# 
# # Create a matrix.
# 
# # Display:
# 
# # Shape
# # Number of dimensions
# # Transpose
# # Transposed shape
# 
# # Then explain what changed.
# 
# import numpy as np
# 
# matrix=np.array([
    # [1,2,3],
    # [4,5,6]
# ])
# 
# print("Shape is :",matrix.shape)
# print("No.of Dimensions :",matrix.ndim)
# t_matrix=np.transpose(matrix)
# print("\nTranspose Matrix is :\n",t_matrix)
# print("Shape of Transpose Matrix is :",t_matrix.shape)


# # Program 4 — Vector Norm & Distance

# # Create two vectors.

# # Calculate:

# # Norm of each vector.
# # Euclidean distance between them.

# # Don't just use functions—understand the mathematical formula you're implementing.

# import numpy as np

# vec1=np.array([1,2,3])
# vec2=np.array([4,5,6])



# # Norm of each vector.

# norm1=np.linalg.norm(vec1)
# norm2=np.linalg.norm(vec2)

# print("\nNorm 1 :",norm1)
# print("\nNorm 2 :",norm2)

# # Euclidean distance between them.

# dist=np.linalg.norm(vec2-vec1)

# print("\nDistance Between two vectors :",dist)

# # Program 5 — NumPy Linear Algebra Practice

# # Create a small matrix and explore:

# # Matrix multiplication
# # Transpose
# # Determinant
# # Inverse

# # Use:

# # np.linalg

# # You don't need to manually calculate determinant/inverse yet, but understand what they represent.

# import numpy as np

# A = np.array([
    # [2, 3],
    # [1, 4]
# ])

# B = np.array([
    # [5, 2],
    # [3, 1]
# ])

# # Matrix multiplication
# print("\nMatrix multiplication :\n",A@B)

# # Transpose
# print("\nTranspose of A :\n",np.transpose(A))

# # Determinant
# det=np.linalg.det(A)
# print("\nDeterminant of A :\n",det)

# # Inverse
# inv=np.linalg.inv(A)
# print("\nInverse of A :\n",inv)



# Program 6 ⭐ — Simple Linear Prediction

# This is the most important program today.

# Imagine:

# Study Hours → Marks

# Represent the input values as a vector/matrix.

# Perform a simple mathematical calculation resembling:

# y=Xw+b

# Don't worry about training a model yet.

# Your goal is to understand that Machine Learning models ultimately perform mathematical operations on vectors and matrices.

import numpy as np
#input
X=np.array([
    [2],
    [4],
    [6]
    ])
# Weight
w=np.array([10])
# Bias
b=5

Xw=X@w
# Prediction
y=Xw + b
print("Predicted Marks :")
print(y)