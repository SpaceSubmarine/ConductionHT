import numpy as np
import matplotlib.pyplot as plt
import math

# Input =============================================
N = 70  # Number of nodes
L = 2  # m
S = 1  # arbitrary surface in m2
delta_x = L / N  # differential length
Vp = S * delta_x  # m3
rho = 2300  # kg/m3
cp = 700  # J/kgK
T_a = 19 + 273  # Kelvin
T_b = 19 + 273  # Kelvin
alpha_ext = 8.5  # W/m2K
lambda_1 = 1.6  # W/mK
max_error = (10 ** (-11))  # Max error Gauss-Seidel
max_iter = 500000  # Maximum number of iterations
T_w = 19 + 273  # Initial Temperature of the cooper in Kelvin
t_step = 500  # Number of time divisions 150

total_time = 100*24*3600  # the total time purposed at the exercise
time = np.linspace(0, total_time, t_step)  # total_time + 1

# Here we define the distance in meters for the walls in a vector
x_wall = np.linspace(0, L, N + 1)  # Value of x at the walls
for i in range(1, N):
    x_wall[i] = i * delta_x

x_wall[0] = 0
x_wall[-1] = L

# Coefficients and temperatures initialization =============================================
domain = np.linspace(0, L, N + 2)
T_dist = np.zeros(len(domain)).astype(int)
T_dist[:] = T_w  # initial temperature of the ground
T_dist[0] = T_a  # initial external temperature
T_dist[-1] = T_b

ae = np.zeros(len(domain))
ae[:] = lambda_1 * S / delta_x
aw = ae.copy()
ap = np.zeros(len(domain))
bp = np.zeros(len(domain))
q_flux = np.zeros(len(domain))

aw[0] = 0
ae[0] = lambda_1 * S / delta_x
ap[0] = (ae[0] * T_dist[1] + bp[0]) / T_dist[0]
ae[N + 1] = 0
aw[N + 1] = lambda_1 * S / delta_x
ap[N + 1] = (aw[N + 1] * T_dist[N] + bp[N + 1]) / T_dist[N]  # i traduced to python
q_flux[0] = alpha_ext * (T_dist[1] - T_dist[0])
bp[0] = q_flux[0] * rho * Vp

A_0 = 19 + 273
A_1 = 5.7 + 273
A_2 = 9.1 + 273
omega_1 = (2 * math.pi / (24 * 3600))
omega_2 = (2 * math.pi / (365 * 24 * 3600))

name = 1
total_iter = 0
stored_diff = []
# =====================================================================================
for t in time:
    plt.ion()
    print("Time step: ", t)

    # Gauss-Seidel=========================================================================
    diff = 100000  # Arbitrary but different from zero
    Iter = 1  # Initializing the number of iterations
    while diff > max_error and Iter < max_iter:
        T_dist_old = T_dist.copy()

        for i in range(1, N + 1):
            # =================================================================
            T_dist[0] = A_0 + A_1 * math.sin(math.radians(omega_1 * t)) + A_2 * math.sin(
                math.radians(omega_2 * t))  # External temperature in time
            # =================================================================
            ap[i] = float(lambda_1 * S / delta_x) + (lambda_1 * S / delta_x)
            aw[i] = float(lambda_1 * S / delta_x)
            ae[i] = float(lambda_1 * S / delta_x)
            bp[i] = -lambda_1 * ((T_dist[i] - T_dist[i - 1]) / delta_x) * Vp
            # =================================================================
            T_dist[i] = float((aw[i] * T_dist[i - 1] + ae[i] * T_dist[i + 1] + bp[i]) / ap[i])

        diff = max(T_dist - T_dist_old)
        stored_diff.append(diff)
        Iter += 1
        total_iter += 1
        print(Iter)
    plt.clf()
    # animated plot
    plt.figure(1)
    plt.plot(domain, T_dist)
    plt.xlabel('Distance (m)')
    plt.axis([0, max(domain), min(T_dist), max(T_dist)])
    plt.ylabel('Temperature (k)')
    plt.savefig("./heat_plot/" + str(name) + ".png")
    plt.ion()


    plt.figure(2)
    plt.imshow((domain, T_dist), aspect='auto', interpolation='gaussian', cmap='inferno')
    plt.colorbar()
    plt.xlabel('Control Volumes')
    plt.autoscale()
    #plt.ylabel('Temperature (k)')
    #plt.autoscale()
    plt.show()
    plt.savefig("./heat_field/" + str(name) + ".png")
    plt.ion()
    plt.pause(0.0001)
    plt.clf()
    name += 1
plt.ioff()  # Plot evolution end

# Final Info print
# ===============================================================
print("===============================================================")
print("Number of nodes: ", N)
print("Number of time steps: ", t_step)
print("Total number of iterations: ", total_iter)
print("External Temp in kelvin (L=0) at final time: ", T_dist[0])
print("Final temperature in Kelvin in x=L/2 at final time: ", T_dist[int(len(T_dist)/2)])
print("Final temperature in Kelvin in x=L at final time: ", T_dist[len(domain)-1])
print("Final time(s): ", t)

# Plot maintain
# ===============================================================
plt.figure(2)
plt.imshow((domain, T_dist), aspect='auto', interpolation='gaussian', cmap='inferno')
plt.autoscale()
plt.colorbar()
plt.xlabel('Control Volumes')
#plt.ylabel('Temperature (k)')
plt.show()

plt.figure(1)
plt.plot(domain, T_dist)
plt.xlabel('Distance (m)')
plt.axis([0, max(domain), min(T_dist), max(T_dist)])
plt.ylabel('Temperature (k)')
plt.show()

# Plots =============================================


