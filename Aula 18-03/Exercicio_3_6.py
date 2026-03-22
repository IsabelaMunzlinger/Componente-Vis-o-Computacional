import cv2
import time

# Carrega o vídeo (ajuste o caminho se necessário)
cap = cv2.VideoCapture(r'./Aula 18-03/Video/paca.mp4')

# Cria o objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Variáveis para o cálculo de FPS
tempo_frame_anterior = 0
tempo_frame_atual = 0

# Controle (booleano) para ligar/desligar o CLAHE
aplicar_clahe = False 

while cap.isOpened():
    ret, frame = cap.read()
    
    # Se o vídeo acabar, encerra o loop
    if not ret:
        break

    # Converte para escala de cinza para aplicar o CLAHE de forma mais leve
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica o processamento dependendo do modo selecionado
    if aplicar_clahe:
        resultado = clahe.apply(gray)
        texto_modo = "Modo: CLAHE (Pressione 'c' para Original)"
    else:
        resultado = gray
        texto_modo = "Modo: Original (Pressione 'c' para CLAHE)"

    # Calcula o FPS matemático
    tempo_frame_atual = time.time()
    # Evita divisão por zero no primeiro frame
    diferenca_tempo = tempo_frame_atual - tempo_frame_anterior
    if diferenca_tempo > 0:
        fps = 1 / diferenca_tempo
    else:
        fps = 0
    tempo_frame_anterior = tempo_frame_atual

    # Escreve o FPS e o Modo na imagem
    cv2.putText(resultado, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(resultado, texto_modo, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Exibe o vídeo
    cv2.imshow('Processamento em Tempo Real', resultado)

    # Captura a tecla pressionada (espera 1 milissegundo)
    tecla = cv2.waitKey(1) & 0xFF
    
    if tecla == ord('q'): # 'q' para sair
        break
    elif tecla == ord('c'): # 'c' para alternar o CLAHE
        aplicar_clahe = not aplicar_clahe

cap.release()
cv2.destroyAllWindows()