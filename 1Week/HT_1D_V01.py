# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:32:51 2022

@author: MARC MONCLUS MONTALVEZ
"""
## Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


print("\n")
print("Imported modules correctly...")
print("\n")
## Input-DATA==============================================================



# creating a 1-D list (Vertical)
#♥list1 = [[10],[20],[30]]


#reminder  
#np.linspace(2.0, 3.0, num=5)
#array([2.  , 2.25, 2.5 , 2.75, 3.  ])

#np.linspace(2.0, 3.0, num=5, endpoint=False)
#array([2. ,  2.2,  2.4,  2.6,  2.8])

#np.linspace(2.0, 3.0, num=5, retstep=True)
#(array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

####################################################
print("Input data correct...")

N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
#x2 = np.linspace(0, 10, N, endpoint=False)


plt.plot(x1, y + 0.5, 'o')

plt.ylim([-0.5, 1])
(-0.5, 1)
plt.show()

print("\n")
print("Test 1 passed")





