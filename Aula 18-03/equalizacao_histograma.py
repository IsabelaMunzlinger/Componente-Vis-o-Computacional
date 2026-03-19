import cv2
import matplotlib.pyplot as plt
import numpy as np

imagem = cv2.imread('./Aula 18-03/Imagens/campo.jpg', 0) #lê a imagem em escala de cinza

#Aplica a equalização do histograma
imagem_eq = cv2.equalizeHist(imagem)

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,5))

hist1, _ = np.histogram(imagem.ravel(), 256, [0,256])
# Calcula cdf
cdf1 = hist1.cumsum() #cumulative distribution function - curva de frequência acumulada
cdf1_norm = cdf1 * hist1.max() / cdf1.max()

ax1.hist(imagem.ravel(), 256, [0,256], color='pink')
ax1.plot(cdf1_norm, color='red')
ax1.set_title('Original + CDF')

# Equalização do histograma
hist2, _ = np.histogram(imagem_eq.ravel(), 256, [0,256])

cdf2 = hist2.cumsum() #cumulative distribution function - curva de frequência acumulada
cdf2_norm = cdf2 * hist2.max() / cdf2.max()

ax2.hist(imagem_eq.ravel(), 256, [0,256], color='pink')
ax2.plot(cdf2_norm, color='red')
ax2.set_title('Equalizada + CDF')

cv2.imshow("Original", imagem)
cv2.imshow("Equalizada", imagem_eq)


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()