import cv2
import numpy as np
import pprint

imagem = cv2.imread("./imagens/puzzle.png", 0)

#Binarização
_, imgBinarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

momentos = cv2.moments(imgBinarizada) #dicionario com os momentos da imagem, que são usados para calcular características invariantes a rotação, escala e translação

pp = pprint.PrettyPrinter(indent=4, sort_dicts=True)
pp.pprint(momentos)