import cv2
import numpy as np
from matplotlib import pyplot as plt

imgOriginal = cv2.imread("./imagens/chaplin2.jpg")

imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

tomClaro = np.array([170, 100, 100])
tomEscuro = np.array([190, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem binarizada", imgSegmentada)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows

