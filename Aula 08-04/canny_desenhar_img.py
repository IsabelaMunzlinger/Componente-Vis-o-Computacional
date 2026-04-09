import cv2
import numpy as np
import random

img = cv2.imread('./imagens/frutas_vetor.jpeg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bordas = cv2.Canny(cinza, 95, 250)

#Vê onde tem contorno e salva no vetor contornos
contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#(imagem, tipo de contorno, metodo de aproximacao(linha toda ou só os pontos))

print(f"Número de contornos: {len(contornos)}")

#metodo hull
for c in contornos:
    if cv2.contourArea(c) > 100:
        hull = cv2.convexHull(c)
        
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(img, [hull], -1, cor, 2) #hull cria a corda envolta da figura

cv2.imshow('Original', img)



cv2.waitKey(0)
cv2.destroyAllWindows() 