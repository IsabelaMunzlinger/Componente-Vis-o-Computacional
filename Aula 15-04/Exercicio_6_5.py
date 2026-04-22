#Implemente um script que utilize o vídeo objetos-coloridos.mov para 
# identificar apenas os objetos de cor azul.

import numpy as np
import cv2

cap = cv2.VideoCapture('./videos/objetos-coloridos.mov')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    tomClaroAzul = np.array([100, 100, 100]) #para a cor azul
    tomEscuroAzul = np.array([140, 255, 255]) #para a cor azul
    imgBinarizadaAzul = cv2.inRange(imgHSV, tomClaroAzul, tomEscuroAzul)
    cv2.imshow('Frame Original', frame)
    cv2.imshow('Frame Binarizado', imgBinarizadaAzul)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
