import cv2
import numpy as np
import pprint

imagem = cv2.imread("./imagens/furo3.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

#Contornos
contornos, hierarquia = cv2.findContours(imgBinarizada, 
                                cv2.RETR_CCOMP, 
                                cv2.CHAIN_APPROX_SIMPLE)

print(hierarquia)

objetos = 0
furos = 0

#range cria um vetor que vai até contornos
for i in range(len(contornos)):
    if hierarquia[0][i][-1] == -1:
        objetos += 1 #Se somar mais um tem pai, se for -1 é porque não tem pai, ou seja, é um objeto
    else:
        furos += 1

euler = objetos - furos

print(f"Furos: {furos}, Objetos:{objetos}, Número de Euler:{euler}")
