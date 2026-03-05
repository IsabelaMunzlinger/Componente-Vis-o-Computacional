import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('./Aula 04-03/Video/objetos-coloridos.mov')



while True:

    ret, frame = cap.read() #frame vai ser alterado o tempo todo

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converte de rgb para hsv
    h_original, _, _ = cv2.split(hsv) #por padrão coloca underline quando não usa
    h_visual_original = cv2.applyColorMap(h_original, cv2.COLORMAP_SPRING)

    cv2.imshow('Webcam em tempo real', h_visual_original)

    if cv2.waitKey(1000//30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
