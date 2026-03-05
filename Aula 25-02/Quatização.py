import cv2
import numpy as np

imagem = cv2.imread("./Aula 25-02/Imagens/chaplin.jpg")

k = 12 #degrau da cor
intervalo = 256//k #duas barras trunca o valor depois da vírgula

img_quantizada = (imagem//intervalo)*intervalo
#// trunca os valores, só pega antes da vírgula, depois de reduzir (imagem//intervalo), ele retorna pro valor original, multiplicando novamente pelo valor do intervalo

print(type(intervalo))
print(str(intervalo))

cv2.imshow("Chaplin", imagem)
cv2.imshow("Chaplin2", img_quantizada)
cv2.waitKey(0)
cv2.destroyAllWindows()