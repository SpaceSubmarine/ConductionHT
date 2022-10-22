import os 
os.system('cls')
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt 


## Input-Data ==============================================
#physical data:

thick = 3 #m
heigh = 2 #m
width = 1 #m
sw = width*heigh #m2
se=sw #m2
density = 8830 #kg/m3
Vp=thick*heigh*width #m3

T_a = 2
T_b = 2000
alpha_a = 25000 #W/(m^2 k)
alpha_b = 2000 # random number  W/(m^2 k)
q_dot = 3 #have problems 

T_a = T_a+273 # Celsius to Kelvin
T_b = T_b +273 # Celsius to Kelvin
lambda_1 = 386 #W/mK cooper conduction heat transfer at  20ºC

# Numerical Data
N = 5
Max_error = (10**(-10))
T_input = 25
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


T_init = np.ones(N+2)
#Initial Temp of the cooper
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

ap = (lambda_1*sw/dpw) + (lambda_1*se/dpe)
aw = lambda_1*sw/dpw
ae = lambda_1*se/dpw
bp = q_dot * density *Vp



diff = 100000
stored_diff = np.ones(Max_iter)
iteration = 1

while diff > Max_error and iteration < Max_iter:    
    for i in range(1,len(T)-1):        
        
        T_f[i] =  (aw*T[i-1] + ae*T[i+1] + bp)/ap
        
        # vector to plot the error evolution 
        stored_diff[i] = np.max(T-T_f)
        
        diff = np.max(T-T_f)
    
        T = T_f
    
        iteration = iteration+1