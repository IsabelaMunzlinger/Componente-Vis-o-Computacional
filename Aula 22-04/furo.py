import cv2
import numpy as np

imagem = cv2.imread("./imagens/furo3.png")

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Binarização
_, imgBinarizada = cv2.threshold(imagemCinza, 127, 255, cv2.THRESH_BINARY)

contornos, hierarquia = cv2.findContours(imgBinarizada, 
                                         cv2.RETR_CCOMP, 
                                         cv2.CHAIN_APPROX_SIMPLE)

print(hierarquia)

objetos = 0
furos = 0

for i in range(len(contornos)):
    if hierarquia[0][i][-1] == -1:
        # se o ultimo elemento for -1, é um objeto pai
        objetos += 1
    else:
        # se o ultimo for 0, é um elemento filho (nesse caso, um furo no objeto pai)
        furos += 1

euler = objetos - furos

print(f"Furos: {furos}, Objetos: {objetos}, Euler: {euler}")

cv2.imshow("Original", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()