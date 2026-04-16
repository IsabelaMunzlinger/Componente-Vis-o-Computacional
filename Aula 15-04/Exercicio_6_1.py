#Remova a marca d'água da imagem assinatura.png utilizando segmentação de imagens.

import cv2

img = cv2.imread("./imagens/assinatura.png")

metodo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(img, 128, 255, metodo) #imagem, limiar, valor máximo, método

cv2.imshow("Original", img)
cv2.imshow("Binarizada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows