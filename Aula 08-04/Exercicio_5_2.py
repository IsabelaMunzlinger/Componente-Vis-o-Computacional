#Compare visualmente o resultado do Sobel (magnitude combinada) com 
# o algoritmo de Canny da imagem objetos.jpg. 
# Qual deles produz bordas mais finas ("esqueletizadas") e prontas para contagem de objetos?

# O Canny produz bordas mais finas

import cv2

img = cv2.imread('./imagens/objetos.jpg')

imagemCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(imagemCinza, cv2.CV_8U, 1, 0, ksize=3)
sobelx_64 = cv2.Sobel(imagemCinza, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx_64)

sobely = cv2.Sobel(imagemCinza, cv2.CV_8U, 0, 1, ksize=3)
sobely_64 = cv2.Sobel(imagemCinza, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely_64)

sobelCombinado = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

### Canny

imgCanny = cv2.Canny(imagemCinza, 100, 200)


cv2.imshow('Sobel combinado', sobelCombinado)
cv2.imshow('Canny', imgCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()