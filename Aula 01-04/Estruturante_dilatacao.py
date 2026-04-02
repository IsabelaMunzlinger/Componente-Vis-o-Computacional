import cv2

img = cv2.imread('./imagens/rolamento.png', 0)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

imgProcessada = cv2.dilate(img, elementoEstruturante, iterations=5)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()