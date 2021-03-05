
"""
author :Ranjit
created date : 3/3/2021
updated date : 3/3/2021
title : Reverse the array
"""


import numpy as np

array_list = np.arange(12,38)
print("the Original List"+str(array_list))

array_list = array_list[ : :-1]
print("Reverse array list "+str(array_list))