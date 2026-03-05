import cv2

img = cv2.imread('./Imagens/unoesc.png')

cv2.imwrite('./Imagens/lossy.jpg', img)
cv2.imwrite('./Imagens/lossless.bmp', img)