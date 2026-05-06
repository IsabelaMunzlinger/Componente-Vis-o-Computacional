#Utilizando as imagens tampas1.png e tampas2.png, desenvolva um algoritmo em 
# Python que realize a contagem seletiva de objetos. 
# O sistema deve ser capaz de diferenciar e imprimir separadamente a quantidade de 
# tampas verdes e tampas vermelhas presentes na cena.

import cv2
import numpy as np

def contar_tampas_por_cor(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    if img is None:
        return None

    # 1. Converte para HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 2. Define os limites para o Vermelho (ajustado para detectar tons claros e escuros)
    # O vermelho "dobra" no círculo do Hue (perto de 0 e perto de 180)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)

    # 3. Define os limites para o Verde
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 4. Limpeza morfológica (remove ruídos e buraquinhos nas máscaras)
    kernel = np.ones((5,5), np.uint8)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    # 5. Contagem usando Connected Components
    num_red, _ = cv2.connectedComponents(mask_red)
    num_green, _ = cv2.connectedComponents(mask_green)

    # O num_labels inclui o fundo, então subtraímos 1
    return num_red - 1, num_green - 1

# Processando as imagens
arquivos = ['./imagens/tampinhas1.png', './imagens/tampinhas2.png']

for i, arq in enumerate(arquivos, 1):
    resultado = contar_tampas_por_cor(arq)
    if resultado:
        venda, verde = resultado
        print(f"--- Imagem {i} ---")
        print(f"Tampas Vermelhas: {venda}")
        print(f"Tampas Verdes: {verde}")
        print(f"Total nesta cena: {venda + verde}\n")