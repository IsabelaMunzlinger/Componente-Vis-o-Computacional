import cv2 
from ultralytics import YOLO

model = YOLO('yolo26s.pt')

pegar_Webcam = cv2.VideoCapture(0)
while True: 
    ret, frame = pegar_Webcam.read()
    if not ret:
        break

    results = model(frame, conf=0.5)

    for r in results:
        imagem_anotada = r.plot()
    
    cv2.imshow('Webcam Anotada', imagem_anotada)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
