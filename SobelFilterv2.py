# -*- coding: utf-8 -*-
'''
Mesmo que a v1, mas em grayscale
'''
from PIL import Image
import numpy as np
import time

def inicializa(matriz_in):
    '''
    Opcional: zero padding
    '''
    x,y,z = np.shape(matriz_in)
    matriz_out = np.zeros((x+2,y+2,z), dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            matriz_out[i+1][j+1]=matriz_in[i][j]
    return matriz_out

def converttograyscale(matriz_in):
    x,y,z = np.shape(matriz_in)
    matriz_out = np.zeros((x,y), dtype=np.uint8)
    for j in range(x):
        for k in range(y):
            matriz_out[j,k]=np.round(np.mean(matriz_in[j,k,:]))
    return matriz_out

def correl(m0, m1, m2):
    '''
    m0 e m1: filtros 3x3 vertical e horizontal
    m2: matriz a ser filtrada
    '''
    x,y = np.shape(m2)
    result=np.zeros((x-2,y-2), dtype=np.uint8)
    for j in range(x-2):
        for k in range(y-2):
            submatriz = np.array([
                                  [m2[j  ,k],m2[j  ,k+1],m2[j  ,k+2]],
                                  [m2[j+1,k],m2[j+1,k+1],m2[j+1,k+2]],
                                  [m2[j+2,k],m2[j+2,k+1],m2[j+2,k+2]]
                                 ])
            result[j,k] = np.sqrt((sum(np.sum(m0 * submatriz, axis=1)))**2 + 
                                  (sum(np.sum(m1 * submatriz, axis=1)))**2)
    result = np.clip(np.round(result),a_min=0,a_max=255)
    return result

def main():
    dx = np.array ([
                        [-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]
                   ])
    dy = np.transpose(dx)
    image = Image.open("C:\\Users\\F9910101\\Pictures\\Mario.jpg")
    immatriz = np.array(image)
    tic = time.time()
    temp=converttograyscale(immatriz)
    toc = time.time()
    print("Elapsed time is " + str(toc-tic)+ " seconds.")
    del immatriz
    tic = time.time()
    result=correl(dx,dy,temp)
    toc = time.time()
    del temp
    print("Elapsed time is " + str(toc-tic)+ " seconds.")
    img = Image.fromarray(result)
    img.show()

main()


