#Crie um sistema de inspeção de peças. 
# O algoritmo deve analisar as imagens parafusos1.png, parafusos2.png e parafusos3.png.
#  O sistema deve desenhar um quadrado verde sobre as peças com apenas um furo com a escrita 
# "OK" e um retangulo vermelho com a escrita "Defeito" sobra as peças sem furo ou com mais 
# de um furo.

import cv2
import numpy as np

# Lista de imagens
arquivos = ["./imagens/parafusos1.png", "./imagens/parafusos2.png", "./imagens/parafusos3.png"]

for arq in arquivos:
    img = cv2.imread(arq)
    if img is None: continue
    
    img_result = img.copy()
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Suavização leve para não perder o detalhe do furo
    blur = cv2.GaussianBlur(cinza, (5, 5), 0)

    # 2. Threshold de Otsu (Inverso para objeto ficar branco e fundo preto)
    _, bin = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 3. Morfologia Ajustada
    # Usamos um kernel menor (5x5) para não "engolir" os furos reais
    kernel = np.ones((5, 5), np.uint8)
    # OPEN: remove pontinhos brancos fora das peças (ruído)
    bin_limpa = cv2.morphologyEx(bin, cv2.MORPH_OPEN, kernel)
    # CLOSE: junta partes da peça sem fechar o buraco central
    bin_limpa = cv2.morphologyEx(bin_limpa, cv2.MORPH_CLOSE, kernel)

    contornos, hierarquia = cv2.findContours(bin_limpa, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    if hierarquia is not None:
        hierarquia = hierarquia[0]
        contagem_furos = {}

        # Passo 1: Identificar peças (Objetos sem pai)
        for i in range(len(contornos)):
            area_peca = cv2.contourArea(contornos[i])
            if area_peca < 400: # Ignora objetos muito pequenos
                continue

            pai = hierarquia[i][3]
            if pai == -1: # É uma peça principal
                contagem_furos[i] = 0

        # Passo 2: Contar furos (Objetos que têm um pai na lista de peças)
        for i in range(len(contornos)):
            pai = hierarquia[i][3]
            if pai != -1 and pai in contagem_furos:
                area_furo = cv2.contourArea(contornos[i])
                area_pai = cv2.contourArea(contornos[pai])
                
                # FILTRO CRÍTICO: O furo deve ter um tamanho razoável 
                # nem muito pequeno (reflexo) nem muito grande (a própria peça)
                if 50 < area_furo < (area_pai * 0.5):
                    contagem_furos[pai] += 1

        # Passo 3: Desenhar Veredito
        for idx_peca, qtd_furos in contagem_furos.items():
            x, y, w, h = cv2.boundingRect(contornos[idx_peca])
            
            # Se for porca (tem nylon azul), a binarização pode falhar.
            # No seu caso, o critério é: 1 furo = OK
            if qtd_furos == 1:
                cor = (0, 255, 0)
                label = "OK"
            else:
                cor = (0, 0, 255)
                label = "Defeito"

            cv2.rectangle(img_result, (x, y), (x + w, y + h), cor, 2)
            cv2.putText(img_result, f"{label} ({qtd_furos} furos)", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

    cv2.imshow(f"Inspecao Final - {arq}", img_result)
    cv2.waitKey(0)

cv2.destroyAllWindows()