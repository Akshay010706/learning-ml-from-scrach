#creating and numpy array
#to run -- python numpybasic.py
#1.import numpy library
import numpy as np

#2.creating an array
array1 = np.array([1,2,3,4,5])
print(array1)

#type----
type(array1)

#creating 1d array
a = np.array([1,2,3,4,5])
print(a.shape) #------ output - (5,)

#creating 2d array
b= np.array([(1,2,3,4),(5,6,7,8)])
print(b)
print(b.shape)

#matrix with float numbers
c = np.array([(1,2,3,4),(5,6,7,8)],dtype=float) # dtype is equal to float
print(c)
