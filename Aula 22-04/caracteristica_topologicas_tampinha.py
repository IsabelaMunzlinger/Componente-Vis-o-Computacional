import cv2
import numpy as np
import pprint

imagem = cv2.imread("./imagens/tampinhas1.png")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Binarização
_, imgBinarizada = cv2.threshold(imagemCinza, 200, 255, cv2.THRESH_BINARY_INV)


num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(imgBinarizada)
total_tampinhas = num_labels - 1 #-1 porque o 0 é o fundo, ou seja, não é uma tampinha

print(f"Total de tampinhas: {total_tampinhas}")

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    (x,y) = centroids[i]
    print(f"Área: {area}, Centroide: ({x:.2f},{y:.2f})")


#Escalona os intermediarios entre 0 e 255
labels_norm = np.uint8(255*labels/np.max(labels))

colorida = cv2.applyColorMap(labels_norm, cv2.COLORMAP_PINK)
colorida[labels == 0] = [0,0,0]

cv2.imshow("Tampinhas coloridas", colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()