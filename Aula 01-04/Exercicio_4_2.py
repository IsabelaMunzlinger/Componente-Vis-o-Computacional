import cv2

#Aplique o filtro de Mediana na imagem sal_e_pimenta.png. 
# Aumente o tamanho do kernel gradualmente (3, 5, 9). 
# O que acontece com os detalhes finos da imagem conforme o kernel cresce?

# Os detalhes finos da imagem começam a desaparecer à medida que o tamanho do kernel aumenta. 
# Isso ocorre porque o filtro de mediana substitui cada pixel pelo valor mediano dos pixels vizinhos dentro do kernel.
# Com um kernel maior, mais pixels vizinhos são considerados, 
# o que pode levar a uma suavização excessiva da imagem e à perda de detalhes finos, especialmente em áreas com texturas ou bordas nítidas.

img = cv2.imread('./imagens/sal_e_pimenta.png')

imgMedian = cv2.medianBlur(img, 9)

cv2.imshow('Original', img)
cv2.imshow('Mediana', imgMedian)

cv2.waitKey(0)
cv2.destroyAllWindows()
