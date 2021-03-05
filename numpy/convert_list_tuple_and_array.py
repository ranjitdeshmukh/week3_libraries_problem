
"""
author :Ranjit
created date : 3/3/2021
updated date : 3/3/2021
title : Write a Python program to convert a list and tuple into arrays.  List to array
"""

import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print(np.asarray(my_tuple))