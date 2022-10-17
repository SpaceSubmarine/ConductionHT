import os
#clear
os.system('cls')
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


## Input-DATA==============================================================
r1 = 1       #(m)
r2 = 2       #(m)
H=10;       #Height (m)
tol=0.4    #tolerance ()
T_input = 25+273.15 #ºK
maxIter=1e5
maxdifer=1e-6
N = 10 #Number of control volumes

#Heat transfer coefficient
#Water 30 kW/(m2K) 
alpa_A = 30000 #W/(m^2 k)
T_A = 50+273.15 #ºK

#CO2 high pressure
alpa_B = 5000 #W/(m^2 k)
T_B = 250+273.15 #ºK
dom = np.linspace(1, N+2, N+2)
T_init = np.ones(len(dom)+2)

#Initial Temp of the cooper
for i in range(len(T_init)):
    T_init[i] = (T_input)
    
print("The initial Temperature of the material, has the following vector:")
print(T_init)

print("Domain:", dom)
print("Lenght of the domain:", len(dom))
N1_points = len(dom)-2
print("Number of points of the first material:", N1_points,
      "\ntaking into account that the other 2 points are the boundaries")


rw = np.ones(int(len(dom)))
delta_r = (r2-r1)/len(dom)
print ("delta-r:", delta_r)
print("TEST2")
for i in range(len(rw)):
    rw[i] = (dom[i]/delta_r)*i # ESTO NO LO SE PORQUE NO SON DOS MATERIALES OSTIA
    
print("delta_r1:", delta_r, "for  i=1 to N1+N2")
print("rw vector:", rw)

print("TEST2")
#initializing lambda
lmda = np.ones(len(T_init))
#Thermal conductivity initial at steady state
for i in range(len(T_init)):
    
    lmda[i] = (-1.176 
    + 7.915*(10**(-3))*T_init[i] 
    + 1.486*(10**(-5))*T_init[i]**2 
    - 1.317*(10**(-7))*T_init[i]**3 
    + 2.476*(10**(-10))*T_init[i]**4 
    - 1.556*(10**(-13))*T_init[i]**5)

print("The initial conduction coefficient heat transfer of the material, has the following vector:")
print(lmda)


#Postion of the nodes (general)
rp = np.ones(len(dom))
print(len(rp))
for i in range(2,len(rp)):
    rp[i] = (rw[i]+rw[i-1])/2



## Domain==================================================================

#'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'hsv', 'jet
#plt.imshow(dom, interpolation='none', cmap='inferno')

