import cv2
import numpy as np

#elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)) #cria uma matriz 5x5 e cria uma cruz por dentro

#pode criar o elemento estruturante manualmente
elemento = np.array([[1,0,0,0,1],
                     [0,1,0,1,0],
                     [0,0,1,0,0],
                     [0,1,0,1,0],
                     [1,0,0,0,1]])

print(elemento)