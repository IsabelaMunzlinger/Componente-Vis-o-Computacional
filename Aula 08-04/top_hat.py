import cv2
import numpy as np

img = cv2.imread('./imagens/cosmos.jpeg', 0)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25,25)) #25,25 é largura e altura
# filtro bem pequeno para destacar os astros

imgProcessada = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, elementoEstruturante)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()