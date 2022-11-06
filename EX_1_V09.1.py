import os
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
os.system("cls")

# Input =============================================
thick = 30  # m
height = 1  # m
width = 1  # m
sw = width * height  # m2
se = sw
Vp = thick * thick * width  # m3
Cu_density = 8830  # kg/m3

T_a = 25  # Celsius
T_b = 25  # Celsius
T_a = T_a + 273  # Celsius to Kelvin
T_b = T_b + 273  # Celsius to Kelvin
alpha_a = 2000  # W/(m^2 k)
alpha_b = 2000  # W/(m^2 k)
q_dot = 0.05   # internal energy generation (can be by joule effect...)
Cu_lambda = 386  # W/mK cooper conduction heat transfer at  20ºC

N = 20  # Number of points N
max_error = (10**(-7))  # Max error Gauss-Seidel
max_iter = 500000  # Maximum number of iterations
T_input = 500  # Initial Temperature of the cooper in Celsius
delta_x = thick/N


# Here we define the distance in meters for the walls in a vector
x_wall = np.ones((N+1))  # Value of x at the walls
for i in range(1, N):
    x_wall[i] = i * delta_x

x_wall[0] = 0
x_wall[-1] = thick


# Value of x in the central points
x_point = np.zeros((N + 2))
x_point[0] = delta_x
x_point[1] = (x_wall[1] - x_wall[0]) / 2
for i in range(2, N + 1):
    x_point[i] = x_point[i - 1] + (x_wall[i] - x_wall[i - 1])

x_point[0] = 0
x_point[-1] = thick


# Initial temp of the cooper along x-axis
T_initial = np.ones(N+2)
for i in range(len(T_initial)):
    T_initial[i] = T_input


# Coefficients =============================================
dpw = delta_x
dpe = delta_x

# initializing coefficients 
ap = np.zeros(len(T_initial))
aw = np.zeros(len(T_initial))
ae = np.zeros(len(T_initial))
bp = np.zeros(len(T_initial))

# need to make an error vector

for i in range(len(ap)):
    ap[i] = (Cu_lambda * sw / dpw) + (Cu_lambda * se / dpe)
    aw[i] = Cu_lambda * sw / dpw
    ae[i] = Cu_lambda * se / dpw
    bp[i] = q_dot * Cu_density * Vp

diff = 100000  # Arbitrary but different from zero
stored_diff = np.ones(max_iter)
iteration = 1  # Initializing the number of iterations


T = T_initial
T_f = np.ones(len(T))
# Gauss-Seidel =============================================
while diff > max_error and iteration < max_iter:
    for i in range(1, N + 1):
        T[0] = (ae[0] * T[1] + bp[0]) / ap[0]
        T[-1] = (aw[-1] * T[-2] + bp[-1]) / ap[-1]
        T_f[i] = (aw[i] * T[i - 1] + ae[i] * T[i + 1] + bp[i]) / ap[i]

    stored_diff[1] = np.max(T-T_f)
    diff = float(np.max(abs(T-T_f)))
    iteration += 1
    T = T_f

print("Number of iterations: ", iteration)

# Plots =============================================
fig1, ax = plt.subplots()
plt.imshow((x_point, T), interpolation='none', cmap='inferno')
plt.colorbar()
plt.show()

fig2, ax2 = plt.subplots()
plt.stackplot(x_point, T)
# plt.y_scale("log")
plt.show()
