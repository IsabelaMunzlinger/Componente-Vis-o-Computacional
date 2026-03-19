import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("./Aula 18-03/Imagens/folha_cinza.png", cv2.COLOR_BGR2GRAY)


hist = imagem.ravel() #converte uma matriz para um vetor

#Plota o histograma
plt.hist(hist,256,[0,256], color = 'pink') #precisa passar o número de bins e o intervalo de valores, e o range de valores (0-255)
plt.title('Distribuição  de tons de cinza')
plt.xlabel('Intensidade do pixel')
plt.ylabel('Quantidade de pixels')

plt.tight_layout() #ajusta o layout para evitar sobreposição de elementos
plt.show()