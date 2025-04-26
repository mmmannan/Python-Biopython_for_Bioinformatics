#Week 7
#Exercises

import numpy as np

#Exercise 1
v = np.array([1, 8, 12, 23, 30, 34, 45, 56, 60])
print(v)


#Exercise 2
odd_array = v[0::2]
print(odd_array)


#Exercise 3
backward = v[-1::-1]
print(backward)


#Exercise 4
# The output of the given code will be 2


#Exercise 5
m = np.array([[1, 2, 3, 4, 5],
              [11, 12, 13, 14, 15],
              [21, 22, 23, 24, 25],
              [31, 32, 33, 34, 35],
              [41, 42, 43, 44, 45]])
print(m)


#Exercise 6
m_6 = m[:,-1::-1] 
print(m_6)


#Exercise 7
m_7 = m[-1::-1, :]
print(m_7)


#Exercise 8
mxyz = m[:,-1::-1]
m_8 = mxyz[-1::-1,:]
print(m_8)


#Exercise 9
dimensions = m.shape
rows, cols = dimensions

m_9 = m[1:rows-1, 1:cols-1]
print(m_9)















