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
imgBlur = cv2.GaussianBlur(imgClahe, (9, 9), 0)

#Processamento
# Usa elemento estruturante menor para preservar detalhes finos
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
imgTopHat = cv2.morphologyEx(imgBlur, cv2.MORPH_TOPHAT, elementoEstruturante)

# Inverte e aplica threshold para melhor segmentação
imgProcessada = cv2.addWeighted(imgBlur, 0.8, imgTopHat, 0.5, 0)

#Segmentação usando threshold de Otsu
ret, imgSegmentada = cv2.threshold(imgProcessada, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Limpeza morfológica para remover ruído e preencher pequenos buracos
elementoLimpeza = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
imgSegmentada = cv2.morphologyEx(imgSegmentada, cv2.MORPH_CLOSE, elementoLimpeza, iterations=2)
imgSegmentada = cv2.morphologyEx(imgSegmentada, cv2.MORPH_OPEN, elementoLimpeza, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Cinza CLAHE", imgClahe)
cv2.imshow("Processada", imgProcessada)
cv2.imshow("Segmentada", imgSegmentada)
cv2.waitKey(0)
cv2.destroyAllWindows