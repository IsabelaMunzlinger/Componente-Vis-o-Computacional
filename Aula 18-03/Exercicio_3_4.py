import cv2
import matplotlib.pyplot as plt
import numpy as np

# Usei o 'r' antes do caminho para evitar aquele erro de leitura de arquivo!
imagem = cv2.imread(r'./Aula 18-03/Imagens/ovelha.png', 0) 

# Aplica o CLAHE com os 3 limites diferentes pedidos na questão
# Dica: o padrão comum para tileGridSize é (8,8), mas (20,20) funciona se a imagem for bem grande
clahe_1 = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8,8))
img_clahe_1 = clahe_1.apply(imagem)

clahe_2 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe_2 = clahe_2.apply(imagem)

clahe_5 = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
img_clahe_5 = clahe_5.apply(imagem)

# Preparando a visualização com Matplotlib (para os histogramas)
fig, eixos = plt.subplots(1, 3, figsize=(20, 5)) 
fig.suptitle('Comparativo de clipLimit do CLAHE') 

imagens = [img_clahe_1, img_clahe_2, img_clahe_5] 
titulos = ['CLAHE 1.0', 'CLAHE 2.0', 'CLAHE 5.0']

for i in range(3):
    eixos[i].hist(imagens[i].ravel(), 256, [0,256], color='pink')
    eixos[i].set_title(f"Histograma {titulos[i]}")

# Exibindo as imagens lado a lado com o OpenCV
cv2.imshow('CLAHE 1.0 | CLAHE 2.0 | CLAHE 5.0', np.hstack(imagens))

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()