"""
@author : Ranjit
Created Date : 3/3/2021
Updated Date : 3/3/2021
Title : Write a Python program compare two arrays using numpy.
"""

import numpy as np

array1 = np.array([1,2])
array2 = np.array([2,3])

print("a > b")
print(np.greater(array1,array2))
print("a >= b")
print(np.greater_equal(array1,array2))
print("a < b")
print(np.less(array1,array2))
print("a <= b ")
print(np.less_equal(array1,array2))