import cv2
import numpy as np

imagem = cv2.imread("./Aula 25-02/Imagens/OpenCV_Logo.png")
#Cria array de uma imagem com numpy
#img_np = np.array(imagem) #array numpy, separar as cores por canais

print(type(imagem))

#Separa cada canal para uma cor
#No CV, a ordem é BGR, primeiro o azul, depois o verde e por último o vermelho
b = imagem[:, :, 0]
g = imagem[:, :, 1]
r = imagem[:, :, 2]

#Faz a média de cada canal
np.mean(r) #média dos valores do canal vermelho
cv2.imshow("r", r)
np.mean(g)
cv2.imshow("g", g)
np.mean(b)
cv2.imshow("b", b)

print("Média do canal vermelho: " + str(np.mean(r)))
print("Média do canal verde: " + str(np.mean(g)))
print("Media do canal azul:" + str(np.mean(b)))

cv2.imshow("OpenCS_Logo", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()