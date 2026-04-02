import cv2

img = cv2.imread('./imagens/Noise_SP.png')

imgTratada = cv2.blur(img, (2,2)) #mascara usada para média móvel

cv2.imshow('Original', img)
cv2.imshow('Tratada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()