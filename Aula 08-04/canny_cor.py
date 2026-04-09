import cv2
import numpy as np
import random

img = cv2.imread('./imagens/frutas_vetor.jpeg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bordas = cv2.Canny(cinza, 95, 150)

#Vê onde tem contorno e salva no vetor contornos
contornos, hierarquia = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#(imagem, tipo de contorno, metodo de aproximacao(linha toda ou só os pontos))

imgContornosIsolados = np.zeros_like(img)

print(f"Número de contornos: {len(contornos)}")

for i, c in enumerate(contornos):
    cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(imgContornosIsolados, [c], -1, cor, 2)

cv2.imshow('Original', img)
cv2.imshow('Bordas', bordas)
cv2.imshow('Contornos isolados', imgContornosIsolados)


cv2.waitKey(0)
cv2.destroyAllWindows() 