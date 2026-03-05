import cv2

img = cv2.imread('./Aula 04-03/Imagens/unoesc.png')

cv2.imwrite('./Aula 04-03/Imagens/lossy.jpg', img)
cv2.imwrite('./Aula 04-03/Imagens/lossless.bmp', img)