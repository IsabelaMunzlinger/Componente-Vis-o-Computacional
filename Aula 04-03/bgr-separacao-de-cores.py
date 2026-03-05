import cv2
import numpy as np

imagem = cv2.imread('./Imagens/cores.png')

print(imagem.shape)

#b = imagem[:,:,0] #linha, coluna, canal de cor
#g = imagem[:,:,1]
#r = imagem[:,:,2]

b, g, r = cv2.split(imagem)

cv2.imshow('Imagem original', imagem)
cv2.imshow('Canal b', b)
cv2.imshow('Canal g', g)
cv2.imshow('Canal r', r)
cv2.waitKey(0)
cv2.destroyAllWindows()
