import cv2
import numpy as np
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])

def procesarImagen(imagen):
    imagen = cv2.imread(imagen, 0)
    return imagen

def convolucion(imagen, kernel):

    kernel = np.flipud(np.fliplr(kernel))

    x_kernel = kernel.shape[0]
    y_kernel = kernel.shape[1]
    x_imagen = imagen.shape[0]
    y_imagen = imagen.shape[1]

    x_size = int(((x_imagen - x_kernel)/1)+1)
    y_size = int(((y_imagen - y_kernel)/1)+1)

    img = np.zeros((x_size,y_size))

    for i in range (y_imagen):
        if i > y_imagen - y_kernel:
            break
            if i % 1 == 0:
                for j in range (x_imagen):
                    if j > x_imagen - x_kernel:
                        break
                        if j % 1 == 0:
                            img[j,i] = (kernel * imagen[x: x + x_kernel, y: y + y_kernel]).sum()
                        else:
                            break
    return img

    #main

    imagenFinal = procesarImagen("ejemplo.jpeg")

    img_conv = convolucion(imagenFinal, kernel)
    cv2.imshow("imagen", imagenFinal)