import os
#clear
os.system('cls')
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


## Input-DATA==============================================================
#numerical input=========================================================
N = 10 #Number of control volumes

#Physical input=========================================================
r1 = 1       #(m)
r2 = 2       #(m)
H=10;       #Height (m)
tol=0.4    #tolerance ()
T_input = 25+273.15 #ºK
maxIter=1e5
maxdifer=1e-6
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
    
   
print("The initial Temperature of the material:")
print(T_init, "\n")
print("Domain:", dom, "\n")
print("Lenght of the domain (N+2):", len(dom), "\n")
N_points = len(dom)-2
print("Number of points of the first material (N):", N_points,"\n")


## Domain Discretization==============================================================

delta_r = (r2-r1)/len(dom)
print("delta_r:", delta_r, "for  i=1 to N1+N2\n")


xf = np.ones(len(dom)-1)
for i in range(len(xf)):
    xf[i] = delta_r*(i+1)-delta_r
 
    
### Intento fallido de aplicar la formula
#xp = np.ones(len(dom))
#for i in range(1,len(xp)-1):
#    xp[i] = (xf[i]+xf[i-1])/2
#xp[0]=0


# Hago que la distancia entre los limites y los nodos intenos
# Sean iguales que la distancia entre nodos para simplificar

xp = np.ones(len(dom))
for i in range(len(xp)):
    xp[i] = dom[i]-1
    
xp = np.linspace(0, (r2-r1), N+2)

#plt.plot(xp)
#plt.show


print("TEST1\n")
## Previous Calculations ========================================================

re = np.ones(len(xp))
rw = np.ones(len(xp))
se = np.ones(len(re))
sw = np.ones(len(rw))
for i in range(len(re)):
    rw[i] = xp[i] - delta_r
    re[i] = xp[i] + delta_r
    se[i] = 2*(np.pi)*re[i]*H  
    sw[i] = se[i] 


#problemas en los valores del volumen
vp = np.ones(len(xp))
for i in range(len(vp)):
    vp[i] = np.pi*((re[i]**2)-(rw[i]**2))*H

print("TEST2\n")


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
print(lmda,"\n")

## Domain==================================================================

#'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'hsv', 'jet
#plt.imshow(dom, interpolation='none', cmap='inferno')

