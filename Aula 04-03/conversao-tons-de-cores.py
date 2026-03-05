import cv2
import numpy as np

frutas = cv2.imread('./Aula 04-03/Imagens/frutas.png')
frutas_escuras = cv2.subtract(frutas, (50,50,50,0)) #rgb e alpha
frutas_claras = cv2.add(frutas, (50,50,50,0)) #mais próximo do branco, mais claro

cv2.imwrite('./Aula 04-03/Imagens/frutas_escuras.png', frutas_escuras)
cv2.imwrite('./Aula 04-03/Imagens/frutas_claras.png', frutas_claras)

cv2.imshow('Frutas', frutas)
cv2.waitKey(0)
cv2.imshow('Frutas', frutas_escuras)
cv2.waitKey(0)
cv2.imshow('Frutas', frutas_claras)
cv2.waitKey(0)
cv2.destroyAllWindows()