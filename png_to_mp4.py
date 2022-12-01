import cv2
import os
import time
inicio = time.time()
fps = 20  # fotogramas por segundo
nombre = '221128-Heat_F.mp4'


dir_path = './heat_field/'

count = 0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)

################################################################
path = './heat_plot/'
img_array = []
print(count)
for i in range(1,count):
    filename = str(i)+'.png'
    img = cv2.imread(str(dir_path + filename))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter(nombre, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

fin = time.time()
print("Tiempo de ejecución: ", fin-inicio)