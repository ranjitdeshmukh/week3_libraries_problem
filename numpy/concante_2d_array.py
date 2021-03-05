"""
@author:Ranjit
Created date :4/3/2021
Updated Date : 4/3/2021
Title : concante the 2d array  
"""

import numpy as np
first_array = np.array([[0, 1, 3], [5, 7, 9]])
second_array = np.array([[0, 2, 4], [6, 8, 10]])
result = np.concatenate((first_array, second_array), 0)
print(result)