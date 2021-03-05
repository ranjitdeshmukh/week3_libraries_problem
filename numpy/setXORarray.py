"""
@author : ranjit
created Date : 3/3/2021
Updated Date : 3/3/2021
Title :Write a Python program to find the set exclusive-or
       of two arrays. Set exclusive-or will return the sorted,
       unique values that are in only one (not both) of the input arrays. Array1 
"""
import numpy as np


array1 = np.array([0,10,20,40,60,80])
array2 = np.array([10,30,40,50,70])
print("Set XOR Diff",np.setxor1d(array1,array2))