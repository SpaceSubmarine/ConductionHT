# Librerias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

#No uso esta manera de hacer la mesh por el seaborn
#x = np.array([1, 2, 3, 4, 5])
#y = 1#np.linspace(0,1,3)

#xmesh,ymesh = np.meshgrid(x,y)

############################################################
#Definición de la matriz, y = 1 para una dimension
# el valor de N es input
x = 20
y = 1


heat_matrix = np.z(y, x)





ax = sns.heatmap(heat_matrix, vmin=0, vmax=1)
plt.show()





############################################################
#Documentacion del heatmap con seaborn
# https://pythonbasics.org/seaborn-heatmap/

# Documentacion para heat map con matplot:
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html