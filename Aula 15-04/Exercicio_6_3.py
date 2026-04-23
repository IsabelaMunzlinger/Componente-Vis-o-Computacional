# Utilize métodos de pré-processamento e segmentação de imagens 
# para restaurar a imagem fingerprint.jpg.

import cv2
import numpy as np

img = cv2.imread("./imagens/fingerprint.jpg")

# Converte para escala de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Equalização adaptativa para melhorar contraste local
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
imgClahe = clahe.apply(imgGray)

#Equalização de histograma
imagem_eq = cv2.equalizeHist(imgClahe)

cv2.imshow("Equalizada", imagem_eq)

# Inverte e aplica threshold para melhor segmentação
imgProcessada = cv2.addWeighted(imgClahe, 0.8, imgClahe, 0.5, 0)

imgFiltrada = cv2.Laplacian(imgGray, cv2.CV_8U)
imgFiltrada2 = cv2.Laplacian(imgProcessada, cv2.CV_8U)

imgFinal = cv2.add(imgFiltrada, imgFiltrada2)

cv2.imshow("Original", img)
cv2.imshow("Cinza CLAHE", imgClahe)
cv2.imshow("Processada", imgProcessada)
cv2.imshow("Contornada", imgFiltrada)
cv2.imshow("Soma", imgFinal)
cv2.waitKey(0)
cv2.destroyAllWindows