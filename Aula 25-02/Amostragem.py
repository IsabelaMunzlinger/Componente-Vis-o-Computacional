import cv2
import numpy as np

imagem = cv2.imread("./Aula 25-02/Imagens/chaplin.jpg", cv2.IMREAD_GRAYSCALE)

k = 4 # a cada 4 pixels, ele vai pegar um pixel e alocar em outra imagem, ou seja, vai reduzir a imagem em 4x4
img_reduzida = imagem[::k, ::k] #quantidade de pulos

img_serrilhada = cv2.resize(img_reduzida, (imagem.shape[1], imagem.shape[0]),interpolation=cv2.INTER_NEAREST) #vai ficar serrilahdo porque vai pegar a cor de um pixel e alocar em outra imagem de 4x4


print("Imagem escala redizida:")
print(img_reduzida.shape)
print(type(img_reduzida))
print(img_reduzida.dtype)


print("Imagem serrilhada:")
print(img_serrilhada.shape)
print(type(img_serrilhada))
print(img_serrilhada.dtype)


cv2.imshow("Chaplin cinza", imagem)
cv2.imshow("Chaplin reduzida", img_reduzida)
#imagem com aliasing, ou seja, com serrilhado
cv2.imshow("Chaplin serrilhada", img_serrilhada)

cv2.waitKey(0)
cv2.destroyAllWindows()