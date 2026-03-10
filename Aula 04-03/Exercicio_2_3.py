import cv2

imagem_lossy = cv2.imread("./Aula 04-03/Imagens/lossy.jpg")
imagem_lossless = cv2.imread("./Aula 04-03/Imagens/lossless.bmp")


#subtracao = cv2.bitwise_and(imagem_lossless, imagem_lossy, mask=None)
subtracao = cv2.absdiff(imagem_lossless, imagem_lossy)

resultado = cv2.applyColorMap(subtracao, cv2.COLORMAP_JET)

cv2.imshow('Resultado', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()