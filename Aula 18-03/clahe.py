import cv2
import matplotlib.pyplot as plt
import numpy as np

imagem = cv2.imread('./Aula 18-03/Imagens/ovelha.png', 0) #lê a imagem em escala de cinza

#Aplica a equalização do histograma
imagem_eq = cv2.equalizeHist(imagem)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(20,20))
imagem_clahe = clahe.apply(imagem)

fig, eixos = plt.subplots(1,3, figsize=(17,5)) #eixo é uma tupla, de n posições
fig.suptitle('Comparativo: Original / Global / CLAHE') #quando usa subplots, usa suptitle

imagens = [imagem, imagem_eq, imagem_clahe] #vetor de imagens
titulos = ['Original', 'Global', 'CLAHE']

for i in range(3):
    eixos[i].hist(imagens[i].ravel(), 256, [0,256], color='pink')
    eixos[i].set_title(f"Histograma {titulos[i]}")

cv2.imshow('Original | Global | CLAHE', np.hstack(imagens))

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()