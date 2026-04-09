import cv2 

img = cv2.imread('./imagens/rolamento.png', 0)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
# Remove o ruído da imagem com a erosão e reconstitui a imagem com a dilatação

imgProcessada = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, elementoEstruturante)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()