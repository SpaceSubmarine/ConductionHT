#install pip
import os
import os.path
os.system('cls')
#random matrix with numpy
import numpy as np



#matriz random con numpy 2D
def random_matrix(n,m):
    return np.random.randint(0,n,(m,n))
    

matrix = random_matrix(10,10)

print(matrix)

# plot 2D matrix
import matplotlib.pyplot as plt
plt.imshow(matrix)
plt.show()


