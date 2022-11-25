import numpy as np
import matplotlib.pyplot as plt
# https://www.mathworks.com/matlabcentral/answers/558454-1-d-transient-heat-conduction-with-no-heat-generation-fdm-crank-nicholson


n = 5  # number of nodes
L = 1  # length of domain

A = np.zeros([n, n])
B = np.zeros([n, n])
Bx = np.zeros([n, 1])
Ta = np.zeros([n, 1])
Tb = np.zeros([n, 1])

dx = L / (n - 1)  # domain element
dt = 20  # time step
tmax = 4000  # total time steps (s)
t = np.linspace(0, tmax, int(tmax / dt))  # tmax/dt = numero de timesteps
Tl = 100  # temperature at left face
Tr = 100  # temperature at right face

x = np.linspace(0, L, n)   # linarly spaced vectors x direction
alpha = 1**(-4)  # thermal diffusivity (m^2/s)
r = alpha * dt / (2 * dx**2)   # for usability, must be 0.5 or less

# set up matrix

for i in range(1, n-1):
    A[i, i-1] = -r
    A[i, i] = (1+2*r)  # implicit
    A[i, i+1] = -r
A[0, 0] = 1
A[n-1, n-1] = 1

for j in range(1, n-1):
    B[j, j-1] = r
    B[j, j] = (1-2*r)
    B[j, j+1] = r
B[0, 0] = 1
B[n-1, n-1] = 1

# Boundary condition
print(Bx)
Bx[0, 0] = Tl  # Left Wall (Dirichlet conditions)
Bx[n-1, 0] = Tr  # Right Wall (Dirichlet conditions)

'''# Solution
for i in range(0, n-2):
    Bx[i, 0] = Tb[i, 0]
    Tb[i, 0] = B[i, 0] * Bx[i, 0]
for k in range(1, len(t)):
    print("Time: ", k-1)'''

# Solution
for k in range(1, len(t)):
    Tb[k] = B[k, k] * Bx[k]
    Ta[k] = A[k, k]/Tb[k]  # solve CN Matrix
    for i in range(1, n - 2):
        Bx[i, 0] = Tb[i, 0]
        Tb[i, 0] = B[i, 0] * Bx[i, 0]




print(Ta)
print(A)
print(Tb)
Ta = np.array(A)/np.array(Tb)  #CN Matrix

# plot

plt.plot(x, Ta)
