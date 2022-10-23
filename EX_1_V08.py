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

print('Enter temperature of the first fluid '
    'T_a in Celsius:')
T_a = int(input())
#T_a = 25
print('Enter temperature of the second fluid T_b'
    ' in Celsius:')
T_b = int(input())
#T_b = 25
print('Enter the convection heat transfer '
    'coefficient of the first fluid "alpha_a":')
alpha_a = int(input())
#alpha_a = 2000 #W/(m^2 k)
print('Enter convection heat transfer coefficient '
    'of the second fluid "alpha_b":')
alpha_b = int(input())
#alpha_b = 2000 # random number  W/(m^2 k)
print("Enter the internal heat energy 'q_dot_u' "
    "(constant) of the solid material:")
alpha_b = float(input())
q_dot = 0.00030 #have problems 

T_a = T_a+273 # Celsius to Kelvin
T_b = T_b +273 # Celsius to Kelvin

print('Introduce the conduction heat transfer '
    'value (constant), of the chosen material '
    'in W/mK :')
lambda_1 = int(input())
#lambda_1 = 386 #W/mK cooper conduction heat transfer at  20ºC

# Numerical Data
print('Enter the number of points N:')
N = int(input())
# N = 10
Max_error = (10**(-18))
print('Enter the temperature of the solid '
    'material in Celsius:')
#T_b = int(input())
T_input = int(input())
#T_input = 250
T_input = T_input+273
Max_iter =500000


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


diff = 100000
stored_diff = np.ones(Max_iter)
iteration = 1


#GAUSS-SEIDEL
while diff > Max_error and iteration < Max_iter:
    for i in range(1,N+1):
        T[0] = T_a#(ae[0]*T[1]+bp[0]) / ap[0]
        T[-1] = T_b#(aw[-1]*T[-2]+bp[-1]) / ap[-1]
        T_f[i] =  (aw[i]*T[i-1] + ae[i]*T[i+1] + bp[i])/ap[i]
        
    iteration = iteration + 1
    stored_diff[i] = np.max(T-T_f)
    diff = float(np.max(abs(T-T_f)))
    T=T_f


print("Number of iterations:", iteration)
if iteration < 50:
    print("The number of iterations seems to be very lower."
    "Maybe the code has something wrong with the coefficients"
    " or with the Gauss-Seidel method")


fig1, ax = plt.subplots()
plt.imshow((x_point,T), interpolation='none', cmap='inferno')
plt.colorbar()
plt.show()

fig2, ax = plt.subplots()
plt.stackplot(x_point,T)
#plt.yscale("log")
plt.show()

