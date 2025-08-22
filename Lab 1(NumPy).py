import numpy as np


#creating and inspecting arrays
a = np.array([1, 2, 3])      
b = np.array([[1, 2], [3, 4]])
print(a.shape) 
print(b.shape) 
print()

#Array Operations
c = np.array([10, 20, 30]) 
d = np.array([1, 2, 3]) 
print(c + d) 
print()

#Broadcasting
x = np.array([[1,2,3],[4,5,6]])
y = np.array([10,20,30])
print(x+y)
print()
