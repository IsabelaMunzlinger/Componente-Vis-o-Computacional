import cv2
import numpy as np
import pprint
import math

imagem = cv2.imread("./imagens/puzzle.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

momentos = cv2.moments(imgBinarizada) #dicionario com os momentos da imagem, que são usados para calcular características invariantes a rotação, escala e translação
momentosHu = cv2.HuMoments(momentos) #calcula os momentos de Hu, que são invariantes a rotação, escala e translação

centroide_x = int(momentos["m10"] // momentos["m00"]) #dicionario passa o valor do momento em ""
centroide_y = int(momentos["m01"] // momentos["m00"])

#atan2, 2 argumentos
angulo_rad = 0.5 * math.atan2(2 * momentos["mu11"], momentos["mu20"] - momentos["mu02"])

angulo_graus = math.degrees(angulo_rad)

print(f"Centroide X: {centroide_x}, Centroide Y: {centroide_y}, ângulo: {angulo_graus}")