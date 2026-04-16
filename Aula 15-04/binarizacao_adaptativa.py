import cv2
import numpy as np
from matplotlib import pyplot as plt

imgOriginal = cv2.imread("./imagens/fotografo.png", 0)

metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
ret, imgBinarizada = cv2.threshold(imgOriginal, 200, 255, metodo) 

imgAdaptativa = cv2.adaptiveThreshold(imgOriginal, 255, 
                                      cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY_INV, 31, 5) #31 é o tamanho da matriz

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem binarizada", imgBinarizada)
cv2.imshow("Imagem adaptativa", imgAdaptativa)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows

