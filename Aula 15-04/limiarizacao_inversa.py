import cv2
import numpy as np

imgOriginal = cv2.imread("./imagens/fotografo.png")

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imgOriginal, 128, 255, metodo) #imagem, limiar, valor máximo, método

print("Valor de ret: ", ret)

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem binarizada", imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows

