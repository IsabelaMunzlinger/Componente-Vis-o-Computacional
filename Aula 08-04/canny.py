import cv2

img = cv2.imread('./imagens/motor.jpeg', 0)

imgTratada = cv2.Canny(img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Processada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows() 