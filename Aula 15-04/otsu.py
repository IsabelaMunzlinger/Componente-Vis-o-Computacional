import cv2
import numpy as np
from matplotlib import pyplot as plt

imgOriginal = cv2.imread("./imagens/lena.png", 0)

metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

ret, imgBinarizada = cv2.threshold(imgOriginal, 200, 255, metodo) 

plt.hist(imgOriginal.ravel(), 256, color='gray')
plt.axvline(x=ret, color='r', label=f'Limiar {ret}')
plt.title("Histograma")
plt.legend()

print(cv2.THRESH_OTSU)
print("Valor de ret: ", ret)

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem binarizada", imgBinarizada)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows

