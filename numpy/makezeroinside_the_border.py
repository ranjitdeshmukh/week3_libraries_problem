
"""
author :Ranjit
created date : 3/3/2021
updated date : 3/3/2021
title : 
"""

import numpy as np


arr = np.ones((5,5))
print("Original array:"+str(arr))
arr[1:-1,1:-1] = 0
print("1 on the border and 0 inside in the array  "+str(arr))