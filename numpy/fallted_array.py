

"""
@author : Ranjit
Created Date : 3/3/2021
Updated Date : 3/3/2021
Title :  Write a Python program to create a contiguous flattened array. Original array
"""
import numpy as np

array1 = np.array([[10,20,30],[20,40,50]])
print("Original Array",array1)
print("New flattened array :" ,np.ravel(array1))