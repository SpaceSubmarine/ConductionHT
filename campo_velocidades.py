import numpy as np
import matplotlib.pyplot as plt

# Generate data

dimension = 50
x = np.linspace(0, dimension, dimension)
y = np.linspace(0, dimension, dimension)

x_1, y_1 = np.meshgrid(x, y)

random_data = np.random.random((dimension, dimension))

mesh = np.ones((len(x), len(y)))
heat_flx = np.ones((len(x), len(y)))
vx = np.ones((len(x), len(y)))
vy = np.ones((len(x), len(y)))


for i in range(len(y)):
    for j in range(len(x)):
        heat_flx[i][j] = (mesh[i][j])+i**2-np.sqrt(j**4)
        vx[i][j] = heat_flx[i][j]*2
        vy[i][j] = heat_flx[i][j]*3

v = (vx**2+vy**2)**(1/2)

# cmap='inferno' 'plasma' 'magma' 'jet' 'turbo'
# 'YlOrBr' 'YlOrRd' 'OrRd' 'PuRd' 'RdPu' 'BuPu' 'bone' 'autumn'
# 'cool' 'hot' 'gnuplot' 'gnuplot2' 'CMRmap' 'rainwow'
plt.imshow(v, interpolation='none', cmap='turbo')
plt.colorbar()  # Escala de valores

# Create quiver plot
plt.quiver(vx, vy)


plt.show()

