# Utilize métodos de pré-processamento e segmentação de imagens 
# para restaurar a imagem fingerprint.jpg.

import cv2

img = cv2.imread("./imagens/fingerprint.jpg")

# Converte para escala de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Equalização adaptativa para melhorar contraste local
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
imgClahe = clahe.apply(imgGray)

# Suavização para reduzir ruído
imgBlur = cv2.GaussianBlur(imgClahe, (5, 5), 0)

#Processamento
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
imgTopHat = cv2.morphologyEx(imgBlur, cv2.MORPH_TOPHAT, elementoEstruturante)

# Combina o resultado top-hat com a imagem borrada para reforçar as cristas
imgProcessada = cv2.addWeighted(imgBlur, 1.0, imgTopHat, 1.0, 0)

#Segmentação usando threshold de Otsu
ret, imgSegmentada = cv2.threshold(imgProcessada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Original", img)
cv2.imshow("Cinza CLAHE", imgClahe)
cv2.imshow("Processada", imgProcessada)
cv2.imshow("Segmentada", imgSegmentada)
cv2.waitKey(0)
cv2.destroyAllWindows