#Utilize uma imagem sudoku.png. 
# Aplique o a limiarização global e a limiarização adaptativa e compare 
# qual método preservou melhor a legibilidade do texto. Por que isso ocorre?

#O método que melhor preservou a legibilidade foi o Adaptativo, pois ele
# analisa a vizinhança e calcula o limiar para cada pixel, diferente do global que usa só um.

import cv2

imgOriginal = cv2.imread("./imagens/sudoku.png", 0)

#Global
#Limiarização global
metodo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imgOriginal, 128, 255, metodo) #imagem, limiar, valor máximo, método

#Adaptativa
# Limiarização adaptativa gaussiana
thresh = cv2.adaptiveThreshold(imgOriginal, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Global", imgBinarizada)
cv2.imshow("Adaptativa Guassiana", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows