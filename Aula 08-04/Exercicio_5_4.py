#Aplique o filtro de Mediana ou Gaussiano antes de rodar o algoritmo de Canny. 
# Prove através de capturas de tela como a remoção prévia de ruído altera a limpeza das bordas 
# detectadas. Utilize as imagens monumento.png e Noise_SP.png.

import cv2

img = cv2.imread('./imagens/monumento.png', 0)

imgCannySemFiltro = cv2.Canny(img, 100, 200)

imgTratadaGaussiano = cv2.GaussianBlur(img, (5,5), 0) 

imgCanny = cv2.Canny(imgTratadaGaussiano, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Canny sem filtro', imgCannySemFiltro)
cv2.imshow('Tratada', imgTratadaGaussiano)
cv2.imshow('Canny', imgCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
