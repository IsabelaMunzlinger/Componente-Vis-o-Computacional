import cv2
import numpy as np

# Carregamento da imagem do seu arquivo Ex2
img = cv2.imread('./Ex2/sementes.png')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ETAPA 1: Limpeza Completa (1,0 pt)
blur = cv2.GaussianBlur(cinza, (5, 5), 0) # Elimina grãos indesejados
_, bin = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morfologia: Erosão para separar os grãos que estão encostados
kernel = np.ones((3, 3), np.uint8)
bin_separada = cv2.erode(bin, kernel, iterations=2)

# ETAPA 2: Extração de Metadados e Contagem (1,0 pt)
# RETR_CCOMP organiza a hierarquia em objetos (pais) e furos (filhos)[cite: 1]
contornos, hierarquia = cv2.findContours(bin_separada, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

total_graos = 0  # Inicializa o contador

if hierarquia is not None:
    for i in range(len(contornos)):
        # Condição Topológica: Só conta se o contorno não tiver um "pai"[cite: 1]
        if hierarquia[0][i][3] == -1:
            area = cv2.contourArea(contornos[i])
            
            if area > 100: # Filtro de área para evitar contar ruídos como grãos
                total_graos += 1  # Incrementa o contador de grãos
                
                # Extração dos dados exigidos no plano de ensino[cite: 1]
                perimetro = cv2.arcLength(contornos[i], True)
                M = cv2.moments(contornos[i])
                
                # Cálculo do Centroide (Inercial)
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                
                # Momentos de Hu (Inercial)[cite: 1]
                hu = cv2.HuMoments(M).flatten()
                
                # Identificação de furos (Topológica)[cite: 1]
                furos = 0
                filho = hierarquia[0][i][2]
                while filho != -1:
                    furos += 1
                    filho = hierarquia[0][filho][0]

                # Desenha o número do grão e o centroide na imagem para a prova
                cv2.circle(img, (cX, cY), 3, (0, 255, 0), -1)
                cv2.putText(img, f"G{total_graos}", (cX - 10, cY - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

# Imprime o resultado final esperado na Etapa 2[cite: 1]
print("-" * 30)
print(f"CONTAGEM FINAL: {total_graos} grãos")
print("-" * 30)

cv2.imshow("Inspeção de Sementes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()