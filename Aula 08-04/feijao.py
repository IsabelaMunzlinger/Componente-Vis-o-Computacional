import cv2
import numpy as np

# 1. Carregamento e Preparação
# No seu arquivo Ex2, as sementes são escuras em fundo claro
img = cv2.imread('./imagens/teste.png')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ETAPA 1: Limpeza Completa (1,0 pt)
# Suavização para eliminar grãos indesejados antes da segmentação
blur = cv2.GaussianBlur(cinza, (5, 5), 0)

# Binarização de Otsu (Inversa para semente=branco, fundo=preto)
_, bin = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Morfologia Matemática: Separação de objetos encostados usando EROSÃO
kernel = np.ones((3, 3), np.uint8)
img_separada = cv2.erode(bin, kernel, iterations=2) 

# ETAPA 2: Extração de Metadados e Contagem (1,0 pt)[cite: 1]
# RETR_CCOMP organiza a hierarquia em objetos (pais) e furos (filhos)[cite: 1]
contornos, hierarquia = cv2.findContours(img_separada, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

total_graos = 0 # Inicializa o contador de sementes

if hierarquia is not None:
    # Cabeçalho opcional para organização
    print(f"{'--- Relatório de Extração de Metadados ---':^45}\n")
    
    for i in range(len(contornos)):
        # Filtro Topológico: Processa apenas objetos principais (sem pai)[cite: 1]
        if hierarquia[0][i][3] == -1:
            # Características Dimensionais: Cálculo da Área[cite: 1]
            area = cv2.contourArea(contornos[i])
            
            # Filtro de ruído remanescente para precisão dos dados
            if area > 100:
                # Características Inerciais: Momentos de Hu[cite: 1]
                M = cv2.moments(contornos[i])
                
                if M['m00'] != 0:
                    # Cálculo dos Momentos de Hu (invariantes a escala e rotação)[cite: 1]
                    huMoments = cv2.HuMoments(M).flatten()
                    
                    # Características Topológicas: Identificação do número de furos[cite: 1]
                    furos = 0
                    filho = hierarquia[0][i][2] # Primeiro "filho" (furo) do contorno atual
                    while filho != -1:
                        furos += 1
                        filho = hierarquia[0][filho][0] # Próximo furo no mesmo nível

                    # Impressão formatada conforme solicitado para a prova[cite: 1]
                    print(f"Semente {total_graos}: Area={area:.2f}, Furos={furos}, Hu[0]={huMoments[0]:.4f}")
                    
                    total_graos += 1 # Incrementa o contador final

    print(f"\n{'-'*45}")
    print(f"Total de grãos identificados: {total_graos}")

# Mantém a exibição das imagens para validação da limpeza[cite: 1]
cv2.imshow("Original", img)
cv2.imshow("Mascara Binaria Limpa", img_separada)
cv2.waitKey(0)
cv2.destroyAllWindows()