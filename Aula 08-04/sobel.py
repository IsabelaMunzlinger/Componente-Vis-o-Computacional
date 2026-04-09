import cv2
import numpy as np
import random

img = cv2.imread('./imagens/motor.jpeg')

imagemCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(imagemCinza, cv2.CV_8U, 1, 0, ksize=3)
#tamanho 8u, eixo x, eixo y, tamanho do filtro

sobelx_64 = cv2.Sobel(imagemCinza, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx_64) #converte para 8 bits, abs para pegar o valor absoluto, pois o resultado pode ser negativo

#sobelxy = cv2.Sobel(imagemCinza, cv2.CV_8U, 1, 1, ksize=3)
#nao da certo deixar o eixo x e y como 1

sobely = cv2.Sobel(imagemCinza, cv2.CV_8U, 0, 1, ksize=3)

sobely_64 = cv2.Sobel(imagemCinza, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely_64)


#Magia negra hehe
sobelCombinado = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)


cv2.imshow('Original', img)
cv2.imshow('Processada', imagemCinza)
cv2.imshow('Sobel x', sobelx)
cv2.imshow('Sobel y', sobely)
cv2.imshow('Sobel combinado', sobelCombinado)

cv2.waitKey(0)
cv2.destroyAllWindows()