import cv2
import numpy as np
import pprint

imagem = cv2.imread("./imagens/puzzle.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

momentos = cv2.moments(imgBinarizada) #dicionario com os momentos da imagem, que são usados para calcular características invariantes a rotação, escala e translação

momentosHu = cv2.HuMoments(momentos) #calcula os momentos de Hu, é responsável por calcular os momentos de Hu, que são invariantes a rotação, escala e translação, ou seja, eles não mudam se a imagem for rotacionada, redimensionada ou transladada. Esses momentos são usados para descrever a forma de um objeto de maneira que seja independente da sua posição, orientação e tamanho na imagem.

pp = pprint.PrettyPrinter(indent=4, sort_dicts=True)
pp.pprint(momentos)
print(momentosHu)