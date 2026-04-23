import cv2
import numpy as np

imagem = cv2.imread("./imagens/quadrado.png")

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Binarização
_, imgBinarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

contornos, _ = cv2.findContours(imgBinarizada, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)

contorno = contornos[0]

#y cresce para baixo, x cresce para direita.
x, y, w, h = cv2.boundingRect(contorno)
cv2.rectangle(imagem, (x,y), (x+w, y+h), (0, 255, 0), 2)

hull = cv2.convexHull(contorno)
cv2.drawContours(imagem, [hull], -1, (255,0,0),2)

area = int(cv2.contourArea(contorno))
perimetro = int(cv2.arcLength(contorno, True)) # true é se é fechado o contorno ou não
area_caixa_delimitadora = w*h
area_envoltoria_convexa = cv2.contourArea(hull)

#invariantes conforme a distância da camera
proporcao = w/h
extensao = area / area_caixa_delimitadora
solidez = area / area_envoltoria_convexa

#usado para alimentar redes neurais depois
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
print(f"Proporção: {proporcao}")
print(f"Extensão: {extensao}")
print(f"Solidez: {solidez}")

cv2.imshow("Caixa verde Envoltoria azul", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()