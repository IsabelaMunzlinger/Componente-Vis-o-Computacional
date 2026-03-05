import cv2
import numpy as np

imagem = cv2.imread("./Aula 25-02/Imagens/chaplin2.jpg")

imagem_grey = cv2.imread("./Aula 25-02/Imagens/chaplin2.jpg", cv2.IMREAD_GRAYSCALE)

print("Imagem original:")
print(imagem.shape)
print(type(imagem))
print(imagem.dtype) #dtype é a quatização

print("Imagem escala de cinza:")
print(imagem_grey.shape)
print(type(imagem_grey))
print(imagem.dtype)

cv2.imshow("Chaplin", imagem)
#cv2.waitKey(0)

cv2.imshow("Chaplin2", imagem_grey)
cv2.waitKey(0)

cv2.destroyAllWindows()