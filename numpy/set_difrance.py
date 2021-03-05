"""
author : Ranjit
created Date : 3/3/2021
updated Date : 3/3/2021
Title : Write a Python program to find the set difference of two arrays.
         The set difference will return the sorted, unique values in array1 that are not in array2
"""


import numpy as np

array1 = np.array([0,10,20,40,60,80])
print("First array :" ,array1)

array2 = np.array([10,30,40,50,70])

print("set the diffrance two array :", np.setdiff1d(array1,array2))
