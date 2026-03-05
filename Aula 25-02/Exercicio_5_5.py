import cv2
import numpy as np

imagem = cv2.imread("./Aula 25-02/Imagens/OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)

mascara = imagem > 128

binaria = np.zeros_like(imagem)
binaria[mascara] = 255

cv2.imshow("Original", imagem)
cv2.imshow("Binária", binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()

##
# 
# O que aconteceria se você NÃO convertesse?
#Se você tentar fazer imagem > 128 em uma imagem colorida:

#O NumPy vai comparar cada canal separadamente (Azul, Verde e Vermelho).

#O resultado será uma matriz colorida esquisita, onde algumas cores "estouram" e 
# outras somem, mas você não terá uma máscara binária (preto e branco puro).

#Resumo para o seu Projeto:
#Imagens Coloridas (3D): São matrizes de 3 camadas (Altura x Largura x 3).

#Imagens Grayscale (2D): São matrizes de 1 camada (Altura x Largura).

#Para aplicar um limiar (threshold) e criar uma máscara de "forma" ou "silhueta", 
# você precisa de apenas um valor de intensidade por pixel. Por isso, o Grayscale é o 
# primeiro passo obrigatório em quase todo processo de segmentação na Visão Computacional.
##