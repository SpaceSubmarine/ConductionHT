#install pip
import os
import os.path
os.system('cls')
#random matrix with numpy
import numpy as np



#matriz random con numpy 2D
def random_matrix(n,m):
    return np.random.randint(0,n,(m,n))
    

matrix = random_matrix(100,100)

print(matrix)

# plot 2D matrix
import matplotlib.pyplot as plt
plt.imshow(matrix)
plt.show()

matrix2 = np.ones((1000,1000))

for i in range(1000):
    for j in range(1000):
        matrix2[i][j] = (round((i+j)^(2+i)))

plt.imshow(matrix2)
plt.show()

matrix3 = np.ones((1000,1000))

for i in range(1000):
    for j in range(1000):
        matrix3[i][j] = (round((i+j)^(2+(i))*j)) #(round((i+j)^(2+(i)*j)))

plt.imshow(matrix3)
plt.show()