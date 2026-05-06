import cv2
import numpy as np

img = cv2.imread('./imagens/sementes.png')

#### 
# Tratamento da imagem
####

#Converter para a escala de cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar o filtro Gaussiano para remover os ruídos sal e pimenta
imgBlur = cv2.GaussianBlur(imgCinza, (7, 7), 0)

#Usado para aplicar uma máscara na imagem com o filtro
_, bin = cv2.threshold(imgBlur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow("Filtro aplicado", bin)

#Usado para remover espaços entre os grãos
kernel = np.ones((3, 3), np.uint8)
img_separada = cv2.erode(bin, kernel, iterations=2)


#### 
# Encontrar os grãos de feijão e contar eles
####
contornos, hierarquia = cv2.findContours(img_separada, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
total_graos = 0

if hierarquia is not None:
    print(f"{'Sementes':^45}\n")
    
    for i in range(len(contornos)):
        # Somente sementes
        if hierarquia[0][i][3] == -1:
            # Características Dimensionais: Cálculo da Área
            area = cv2.contourArea(contornos[i])
            
            # Filtro de ruído
            if area > 100:
                # Características Inerciais
                M = cv2.moments(contornos[i])
                
                if M['m00'] != 0:
                    # Cálculo dos Momentos de Hu
                    huMoments = cv2.HuMoments(M).flatten()
                    
                    # Informações da quantidade de sementes, e momento de Hu
                    print(f"Semente {total_graos}: Area={area:.2f}, Hu[0]={huMoments[0]:.4f}")
                    
                    total_graos += 1 # Incrementa o contador final

    print(f"\n{'-'*45}")
    print(f"Total de grãos identificados: {total_graos}")




#### 
# Destacar a moeda para selecionar pegar a área dela
####

# Destacar a imagem para mostrar a moeda
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
imgClahe = clahe.apply(imgCinza)

#Equalização de histograma
imagem_eq = cv2.equalizeHist(imgClahe)
#cv2.imshow("Imagem equalizada", imagem_eq)

# Inverte e aplica threshold para melhor segmentação
imgProcessada = cv2.addWeighted(imgClahe, 0.8, imgClahe, 0.5, 0)

imgFiltrada = cv2.Laplacian(imgCinza, cv2.CV_8U)
imgFiltrada2 = cv2.Laplacian(imgProcessada, cv2.CV_8U)

imgFinal = cv2.add(imgFiltrada, imgFiltrada2)

###

#### 
# Encontrar o círculo que representa a moeda para encontrar a área
####
contornos, _ = cv2.findContours(imgFinal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos:
    if cv2.contourArea(contorno) < 500: # Ignora ruídos pequenos
        continue

    #Calculo do perimetro para definir a precisão da aproximação
    perimetro = cv2.arcLength(contorno, True)
    # Aproxima o contorno para um polígono
    epsilon = 0.04 * perimetro
    approx = cv2.approxPolyDP(contorno, epsilon, True)
        
    num_vertices = len(approx)
    x, y, w, h = cv2.boundingRect(approx)
    forma_detectada = "Desconhecido"

    # Lógica de classificação
    if num_vertices == 3:
        forma_detectada = "Triangulo"

    elif num_vertices == 4:
        forma_detectada = "Quadrado"
    else:
        # Se tiver muitos vértices, é um círculo
        forma_detectada = "Circulo"

    cv2.drawContours(bin, [approx], 0, (0, 255, 0), 3)
    cv2.imshow("Equalizada", imagem_eq)

    


cv2.imshow("Sementes", img)
cv2.imshow("Sementes cinzas", imgCinza)
cv2.imshow("Semente filtrada", imgBlur)
cv2.imshow("Thresh", bin)
cv2.imshow("Erosão", img_separada)

print(total_graos)
cv2.waitKey(0)
cv2.destroyAllWindows()