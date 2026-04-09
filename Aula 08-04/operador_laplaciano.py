import cv2
import numpy as np
import random

img = cv2.imread('./imagens/lua.jpeg', 0)

imgFiltrada = cv2.Laplacian(img, cv2.CV_8U)

imgRealcada = cv2.subtract(img, imgFiltrada)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgFiltrada)
cv2.imshow('Realçada', imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()