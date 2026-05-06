import cv2
import numpy as np

img = cv2.imread('./imagens/semafaro_verde.png')

# Para trasnformar para a escala de HSV
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", hsv_frame)

x, y = 133, 413
altura, largura = 90, 413

# A ideia era cortar a imagem para destacar somente o semáforo e ignorar os objetos de fundo
#imagem_cortada = hsv_frame[y : y + altura, x : x + largura].copy()
#cv2.imshow("Teste", imagem_cortada)

#Vermelho
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask_red = cv2.inRange(hsv_frame, lower_red1, upper_red1) + cv2.inRange(hsv_frame, lower_red2, upper_red2)

#Verde
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])
mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)

#Amarelo
tomClaroAmarelo = np.array([20, 100, 100]) #para a cor amarela
tomEscuroAmarelo = np.array([30, 255, 255]) #para a cor amarela
mask_amarelo = cv2.inRange(hsv_frame, tomClaroAmarelo, tomEscuroAmarelo)

# Lista para iterar as cores das máscaras
mascaras = [
    (mask_red, (0, 0, 255), "Vermelho"),
    (mask_green, (0, 255, 0), "Verde"),
    (mask_amarelo, (10, 70, 100), "Amarelo")
    ]

# Procura, com base na tupla de mascaras, as cores na imagem
for mascara, color_draw, label in mascaras:
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) > 600: #Para ignorar áreas menores
            M = cv2.moments(contorno) #Para encontrar o momento
            if M['m00'] != 0:
                # Calcula o centroide
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                    
                # Desenha o centroide e o texto com a cor correspondente
                cv2.circle(hsv_frame, (cX, cY), 7, color_draw, -1)
                cv2.putText(hsv_frame, f"{label}: {cX}, {cY}", (cX - 20, cY - 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_draw, 2)
                print(label)
                if(label == "Verde"):
                    print("SIGA")
               

 
# Mostra o resultado
cv2.imshow('Resultado do semáforo', hsv_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()