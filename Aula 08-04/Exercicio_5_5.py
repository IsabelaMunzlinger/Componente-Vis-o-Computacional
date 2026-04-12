#Crie um script que capture o vídeo da webcam e exiba o resultado de Canny. 
# O desafio é usar a morfologia de Dilatação após o Canny para "engrossar", 
# depois utilize o operador HULL para detectar objetos em frente a câmera. 
# Se não tiver webcam utilize os videos paca.mp4 e leao.mp4.

import random
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #imgSuavizada = cv2.GaussianBlur(frame, (7,7),0)
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(cinza, 50, 150)

    elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    dilatacao = cv2.dilate(imgCanny, elementoEstruturante, iterations=1)

    contornos, hierarquia = cv2.findContours(dilatacao, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
            area = cv2.contourArea(c)
            if area > 3000: # Área mínima para considerar um objeto
                hull = cv2.convexHull(c)
                cor = (0, 255, 0) # Destaque na cor verde
                
                # Desenha no frame o contorno do objeto
                cv2.drawContours(frame, [hull], -1, cor, 2)
                
                #Descrição de objeto detectado
                x, y, w, h = cv2.boundingRect(hull)
                cv2.putText(frame, "Objeto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

    if cv2.waitKey(1000//30) & 0xFF == ord('q'):
        break

    cv2.imshow('Webcam em tempo real', frame)

cap.release()
cv2.destroyAllWindows()
