import cv2

img = cv2.imread('./imagens/placa.png', 0)

#ret, imgProcessada = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#imagem, limiar(maior que 127 vira a cor depois da virgula), cor que vai virar, tipo de limiarização

ret, imgProcessada = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

#ret, imgProcessada = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
#ret porque a função retorna dois valores
#OTSU é um método de limiarização automática

cv2.imshow('Original', img)
cv2.imshow('Processada', imgProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()