import numpy as np

#Create a new array of 2*2 integers, without initializing entries.
x0 = np.empty([2,2], int)
print(x0,'\n')

#Create a new array with the same shape and type as X.
x1 = np.array([[1,2,3], [4,5,6]], np.int32)
np.empty_like(x1)
print(x1, '\n')

#Create a 3-D array with ones on the diagonal and zeros elsewhere.
x2 = np.eye(3)
np.identity(3)
print(x2, '\n')

#Create a new array of 3*2 float numbers, filled with ones.
x3 = np.ones([3,2], float)
print(x3, '\n')

#Create an array of ones with the same shape and type as X.
x4 = np.arange(4, dtype=np.int64)
np.ones_like(x4)
print(x4, '\n')

#Create a new array of 3*2 float numbers, filled with zeros
x5 = np.zeros((3,2), float)
print(x5, '\n')

#Create an array of zeros with the same shape and type as X.
x6 = np.arange(4, dtype=np.int64)
np.zeros_like(x6)
print(x6, '\n')

#Create a new array of 2*5 uints, filled with 6.
x7 = np.full((2, 5), 6, dtype=np.uint)
print(x7, '\n')

x8 = np.ones([2, 5], dtype=np.uint) * 6
print(x8, '\n')

# Create an array of 6's with the same shape and type as X.
x9 = np.arange(4, dtype=np.int64)
print(x9, '\n')
x10 = np.full_like(x9, 6)
print(x10, '\n')

x11 = np.ones_like(x9) * 6
print(x11, '\n')

