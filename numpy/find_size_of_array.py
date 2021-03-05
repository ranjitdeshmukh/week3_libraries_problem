

"""
author :Ranjit
created date : 3/3/2021
updated date : 3/3/2021
title : Write a Python program to convert a list and tuple into arrays.  List to array
"""
import numpy as np
arr = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", arr.size)
print("Length of one array element in bytes: ", arr.itemsize)
print("Total bytes consumed by the elements of the array: ", arr.nbytes)