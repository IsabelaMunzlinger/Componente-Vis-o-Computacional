import cv2
import numpy as np

imgOriginal = cv2.imread("./imagens/fotografo.png")

#poe o valor de 128 onde era acima de 128
metodo = cv2.THRESH_TRUNC
ret, imgBinarizada = cv2.threshold(imgOriginal, 50, 255, metodo)

print("Valor de ret: ", ret)

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem binarizada", imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows

