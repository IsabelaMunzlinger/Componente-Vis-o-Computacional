import cv2
import numpy as np

imagem = cv2.imread("./imagens/quadrado.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

contornos, _ = cv2.findContours(imgBinarizada, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)

contorno = contornos[0]

area = int(cv2.contourArea(contorno))
perimetro = int(cv2.arcLength(contorno, True)) # true é se é fechado o contorno ou não

#usado para alimentar redes neurais depois
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Binarizada", imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()