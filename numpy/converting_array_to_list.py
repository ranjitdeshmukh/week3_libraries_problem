"""
@author: Ranjit
Created Date : 4/3/2021
Updated date : 4/3/2021
Title : Convert array to list 
"""

import numpy as np
arr= np.arange(6).reshape(3, 2)
print("original array",arr)
print('array to list',arr.tolist())