import cv2

#Realize a binarização na imagen lena.png usando um valor fixo (127) e, 
# em seguida, utilize o método de Otsu. Descreva em quais situações 
# o cálculo automático de Otsu se mostra superior ao valor fixo.

#É superior quando você não tem conhecimento prévio sobre a imagem ou quando a iluminação é desigual, 
# pois o método de Otsu calcula automaticamente o limiar ideal com base na distribuição dos pixels,
#  enquanto um valor fixo pode não ser adequado para todas as imagens, especialmente aquelas com variações de iluminação ou contraste. 
# Otsu é particularmente eficaz em imagens com histogramas bimodais, onde há uma clara separação entre os objetos e o fundo.

img = cv2.imread('./imagens/Lena.png', 0)

ret, imgBinarizada = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Binarizada', imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()