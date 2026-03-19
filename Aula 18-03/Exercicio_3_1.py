import cv2
import matplotlib.pyplot as plt
import numpy as np

imagem_clara = cv2.imread("./Aula 18-03/Imagens/casal.png", 0)
imagem_escura = cv2.imread("./Aula 18-03/Imagens/ovelha.png", 0)

imagem_clara_eq = cv2.equalizeHist(imagem_clara)
imagem_escura_eq = cv2.equalizeHist(imagem_escura)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(20,20))
imagem_clara_clahe = clahe.apply(imagem_clara)
imagem_escura_clahe = clahe.apply(imagem_escura)

fig, eixos = plt.subplots(2,3, figsize=(17,10)) #eixo é uma tupla, de n posições
eixos = eixos.flatten()
fig.suptitle('Imagem clara | Imagem escura')

imagens = [imagem_clara, imagem_clara_eq, imagem_clara_clahe, imagem_escura, imagem_escura_eq, imagem_escura_clahe]
titulos = ['Original', 'Global', 'CLAHE', 'Original', 'Global', 'CLAHE']   

for i in range(6):
    eixos[i].hist(imagens[i].ravel(), 256, [0,256], color='pink')
    eixos[i].set_title(f"Histograma {titulos[i]}")

grupo_clara = np.hstack(imagens[:3])
grupo_escura = np.hstack(imagens[3:])

# Exibimos em janelas separadas para evitar o erro de dimensão
cv2.imshow('Imagem Clara: Original | Global | CLAHE', grupo_clara)
cv2.imshow('Imagem Escura: Original | Global | CLAHE', grupo_escura)

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()