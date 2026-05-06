#Desenvolva um algoritmo que processe o arquivo de vídeo objetos-coloridos.mov 
# e realize o rastreamento em tempo real de cada objeto que cruza a tela. 
# Imprima na imagem o centroide do objeto. Ajuste a velocidade do video para que possa 
# ser lida as mensagens.


import cv2
import numpy as np

# Abre o arquivo de vídeo
cap = cv2.VideoCapture('./videos/objetos-coloridos.mov')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Converte para HSV uma única vez (mais eficiente)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. Define os limites para cada cor no espaço HSV
    # Nota: O Vermelho geralmente precisa de dois intervalos pois "quebra" no zero.
    
    # Vermelho (Red)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv2.inRange(hsv_frame, lower_red1, upper_red1) + cv2.inRange(hsv_frame, lower_red2, upper_red2)

    # Verde (Green)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Azul (Blue)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # 3. Combina as máscaras ou processa uma por uma
    # Vamos criar uma lista para iterar e desenhar as informações na tela
    masks = [
        (mask_red, (0, 0, 255), "Vermelho"),    # Máscara, Cor do desenho (BGR), Nome
        (mask_green, (0, 255, 0), "Verde"),
        (mask_blue, (255, 0, 0), "Azul")
    ]

    for mask, color_draw, label in masks:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filtro de ruído
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    # Calcula o centroide
                    cX = int(M['m10'] / M['m00'])
                    cY = int(M['m01'] / M['m00'])
                    
                    # Desenha o centroide e o texto com a cor correspondente
                    cv2.circle(frame, (cX, cY), 7, color_draw, -1)
                    cv2.putText(frame, f"{label}: {cX}, {cY}", (cX - 20, cY - 20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_draw, 2)

    # 4. Exibe o resultado
    cv2.imshow('Rastreamento de Objetos', frame)

    # 5. Ajuste de velocidade: waitKey(ms)
    # Aumente o valor para deixar o vídeo mais lento (ex: 100ms)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()