#Utiliza a imagem cubo_magico.png para criar más caras bináris das cores vermelha, 
# amarela e verde. 
# Após a binarização, aplique técnicas de Morfologia para remover ruídos da máscara. 
# Por fim junte as três imagens em uma. Exiba a imagem original e as quatro imagens binarizadas.

import cv2
import numpy as np

img = cv2.imread('./imagens/cubo_magico.png')

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

tomClaroVermelho = np.array([170, 100, 100]) #para a cor vermelha 
tomEscuroVermelho = np.array([190, 255, 255]) #para a cor vermelha

tomClaroVerde = np.array([40, 100, 100]) #para a cor verde
tomEscuroVerde = np.array([80, 255, 255]) #para a cor verde

tomClaroAmarelo = np.array([20, 100, 100]) #para a cor amarela
tomEscuroAmarelo = np.array([30, 255, 255]) #para a cor amarela

imgBinarizadaVermelho = cv2.inRange(imgHSV, tomClaroVermelho, tomEscuroVermelho)
imgBinarizadaVerde = cv2.inRange(imgHSV, tomClaroVerde, tomEscuroVerde)
imgBinarizadaAmarelo = cv2.inRange(imgHSV, tomClaroAmarelo, tomEscuroAmarelo)


cv2.imshow("Original", img)
cv2.imshow("HSV", imgHSV)
cv2.imshow("Vermelho", imgBinarizadaVermelho)
cv2.imshow("Verde", imgBinarizadaVerde)
cv2.imshow("Amarelo", imgBinarizadaAmarelo)



cv2.waitKey(0)
cv2.destroyAllWindows()