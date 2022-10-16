# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:32:51 2022

@author: MARC MONCLUS MONTALVEZ
"""
## Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

## Input-DATA==============================================================
#r=3.2;        #Radius of the cylinder (m)
#v=8;        #Velocity (m/s)
#dens=1025;  #density of sea water (kg/m3)
#H=10;       #Height (m)
L=20       #lenght (m)
tol=0.4    #tolerance ()
#vOut=v;
T_input = 50
maxIter=1e5
maxdifer=1e-6
X = np.linspace(start = 1,stop = 100,num = 100)
x_df = pd.DataFrame(X)

#generar 
m = x_df*2

aw = np.ones(len(X))
ae = np.ones(len(X))

dimension = 100
x = np.linspace(0, dimension, dimension)
y = np.linspace(0, dimension, dimension)

x_1, y_1 = np.meshgrid(x, y)

random_data = np.random.random((dimension, dimension))

mesh = np.ones((len(x), len(y)))
heat_flx = np.ones((len(x), len(y)))

for i in range(len(y)):
    for j in range(len(x)):
        heat_flx[i][j] = (mesh[i][j])+i**2-np.sqrt(j**4)


#################plot simple
#plt.contour(x_1, y_1, heat_flx, cmap = 'jet')
#plt.colorbar()
#plt.show()


#'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'hsv', 'jet
plt.imshow(heat_flx, interpolation='none', cmap='inferno')
plt.colorbar()
plt.show()