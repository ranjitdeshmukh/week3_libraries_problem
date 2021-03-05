


"""
author :Ranjit
created date : 3/3/2021
updated date : 3/3/2021
title : Write a Python program to convert a list and tuple into arrays.  List to array
"""
import numpy as np
arr = [10, 20, 30]
print("Original array:")
print(arr)
arr = np.append(arr, [[40, 50, 60], [70, 80, 90]])
print("After append values to the end of the array:")
print(arr)