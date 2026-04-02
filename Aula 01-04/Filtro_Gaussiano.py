import cv2

img = cv2.imread('./imagens/olho_halftone.jpg')

imgTratada = cv2.GaussianBlur(img, (5,5), 0) 
#(x,x), y | y é o valor de sigma, que é o desvio padrão da distribuição gaussiana. 
# Se for 0, o OpenCV calcula automaticamente com base no tamanho da máscara.

cv2.imshow('Original', img)
cv2.imshow('Tratada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()