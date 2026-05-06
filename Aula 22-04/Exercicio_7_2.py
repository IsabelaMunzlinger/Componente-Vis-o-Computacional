#Desenvolva um algoritmo, identifique o contorno de cada forma e exiba na tela 
# o nome da figura geométrica detectada. Teste com as figuras quadrado.png, circulo.png 
# e triangulo.png.

import cv2
import numpy as np

# Lista de arquivos para testar
arquivos = ["./imagens/triangulo.png", "./imagens/quadrado.png", "./imagens/circulo.png"]

for caminho in arquivos:
    img = cv2.imread(caminho)
    if img is None:
        print(f"Erro ao carregar: {caminho}")
        continue

    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Suavização para reduzir ruídos antes da binarização
    img_blur = cv2.GaussianBlur(img_cinza, (5, 5), 0)
    _, img_binarizada = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY)

    contornos, _ = cv2.findContours(img_binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) < 100: # Ignora ruídos pequenos
            continue

        # Calculamos o perímetro para definir a precisão da aproximação
        perimetro = cv2.arcLength(contorno, True)
        # Aproxima o contorno para um polígono (o valor 0.04 é a tolerância)
        epsilon = 0.04 * perimetro
        approx = cv2.approxPolyDP(contorno, epsilon, True)
        
        num_vertices = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        forma_detectada = "Desconhecido"

        # Lógica de classificação
        if num_vertices == 3:
            forma_detectada = "Triangulo"
        
        elif num_vertices == 4:
            # Verifica a proporção para diferenciar quadrado de retângulo
            proporcao = float(w) / h
            if 0.95 <= proporcao <= 1.05:
                forma_detectada = "Quadrado"
            else:
                forma_detectada = "Retangulo"
        
        else:
            # Se tiver muitos vértices, é um círculo (ou oval)
            forma_detectada = "Circulo"

        # 1. Desenha o contorno real detectado (em vez da caixa ou hull)
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)

        # 2. Escreve o nome da forma
        cv2.putText(img, forma_detectada, (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        print(f"Arquivo: {caminho} | Vértices: {num_vertices} | Forma: {forma_detectada}")

    cv2.imshow("Detecção de Formas", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()