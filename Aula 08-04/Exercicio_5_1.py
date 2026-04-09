#Aplique o operador de Sobel apenas no eixo X e depois apenas no eixo Y na imagem teclado.png. 
# Descreva quais linhas do teclado (horizontais ou verticais) ficam mais evidentes em cada resultado.

#Tecla de espaço e shift ficaram mais evidentes no eixo y.

import cv2

img = cv2.imread('./imagens/teclado.png')

imagemCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

cv2.imshow('Original', img)
cv2.imshow('Processada', imagemCinza)
cv2.imshow('Sobel x', sobelx)
cv2.imshow('Sobel y', sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()