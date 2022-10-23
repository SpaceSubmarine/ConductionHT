import os 
os.system('cls')
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt 


## Input-Data ==============================================
#physical data:

thick = 30 #m
heigh = 1 #m
width = 1 #m
sw = width*heigh #m2
se=sw #m2
density = 8830 #kg/m3
Vp=thick*heigh*width #m3

print('Enter Ta in Celsius:')
T_a = int(input())
print('Enter Tb in Celsius:')
T_b = int(input())
alpha_a = 2000 #W/(m^2 k)
alpha_b = 2000 # random number  W/(m^2 k)
q_dot = 30 #have problems 

T_a = T_a+273 # Celsius to Kelvin
T_b = T_b +273 # Celsius to Kelvin
lambda_1 = 386 #W/mK cooper conduction heat transfer at  20ºC

# Numerical Data
N = 3
Max_error = (10**(-18))
T_input = 800
T_input = T_input+273
Max_iter =30000


#Domain ==============================================
delta_x = thick/N

# Value of x in the walls
x_wall = np.ones((N+1))

for i in range(1,N):
    x_wall[i] = (i)*delta_x
x_wall[0]=0
x_wall[-1]=thick


#Value of x in the central points
x_point = np.zeros((N+2))
x_point[0] = delta_x
x_point[1] = (x_wall[1]-x_wall[0])/2
for i in range(2,N+1):
    x_point[i] = x_point[i-1]+(x_wall[i]-x_wall[i-1])
    
x_point[0] = 0
x_point[-1] = thick


#Initial Temp of the cooper
T_init = np.ones(N+2)
for i in range(len(T_init)):
    T_init[i] = (T_input)



# Coefficients =============================================

T = T_init
T_f = np.ones(len(T))

dpw = delta_x
dpe = delta_x

# constant thermal coefficient
lambda_1=385 #from tables W/mk

ap = np.zeros(len(T))
aw = np.zeros(len(T))
ae = np.zeros(len(T))
bp = np.zeros(len(T))

for i in range(len(ap)):
    
    ap[i] = (lambda_1*sw/dpw) + (lambda_1*se/dpe)
    aw[i] = lambda_1*sw/dpw
    ae[i] = lambda_1*se/dpw
    bp[i] = q_dot * density *Vp

T[0] = (ae[0]*T[1]+bp[0]) / ap[0]
T[-1] = (aw[-1]*T[-2]+bp[-1]) / ap[-1]

diff = 100000
stored_diff = np.ones(Max_iter)
iteration = 1

#Gauss-Seidel
while diff > Max_error and iteration < Max_iter:    
    for i in range(1,N+1):        
        print(i)
        #T_f[i] =  (aw*T[i-1] + ae*T[i+1] + bp)/ap
        T_f[i] = (ae[i]*T[i+1] + bp[i]) / ap[i]
        
        # vector to plot the error evolution 
    stored_diff[i] = np.max(T-T_f)
    
    diff = np.max(T-T_f)

    T = T_f
    
    #print(iteration)
    print(diff)
    #print("error:", diff<Max_error)
    
    iteration = iteration+1


T[0] = (ae[0]*T[1]+bp[0]) / ap[0]
T[-1] = (aw[-1]*T[-2]+bp[-1]) / ap[-1]        


plt.plot(T)
plt.show()
