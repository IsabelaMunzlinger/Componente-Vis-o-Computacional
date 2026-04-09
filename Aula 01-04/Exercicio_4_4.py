import cv2
import numpy as np

img = cv2.imread('./imagens/engrenagem.png', 0)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8,8))

#MORPH_OPEN é de abertura, melhora a qualidade
imgProcessada = cv2.morphologyEx(img, cv2.MORPH_OPEN, elementoEstruturante)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()