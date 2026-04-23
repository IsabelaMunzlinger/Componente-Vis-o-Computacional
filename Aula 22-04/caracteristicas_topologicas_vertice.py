import cv2
import numpy as np
import pprint

imagem = cv2.imread("./imagens/quadrado.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

#Contornos
contornos, _ = cv2.findContours(imgBinarizada, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)

contorno = contornos[0]

perimetro = int(cv2.arcLength(contorno, True))
poligono = cv2.approxPolyDP(contorno, 0.01*perimetro, True) #aproxima de um poligono

total_vertices = len(poligono)

print(f"Vertices: {total_vertices}")
