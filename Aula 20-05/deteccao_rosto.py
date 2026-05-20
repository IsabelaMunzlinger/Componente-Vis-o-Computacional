import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

imagem = cv2.imread('./imagens/Lena.png')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

rostos = face_cascade.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5)

for(x, y, w, h) in rostos:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(imagem, "Rosto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

    rosto_cinza = cinza[y:y+h, x:x+w]
    
    olhos = eye_cascade.detectMultiScale(rosto_cinza, scaleFactor=1.1, minNeighbors=10)

    for(ex, ey, ew, eh) in olhos:
        cv2.rectangle(imagem, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)


    cv2.imshow('Rosto Detectado', rosto_cinza)

cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


