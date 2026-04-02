import cv2

#Carregue a imagem sal_e_pimenta.png e aplique os filtros de Média e Gaussiano 
# com o mesmo tamanho de kernel (ex: 7x7). Explique por que esses filtros lineares apenas "espalham" 
# o ruído em vez de removê-lo completamente.

#Filtros lineares, funcionam calculando a média ponderada dos pixels vizinhos para cada pixel na imagem.
#Isso não reduz eficientemente o ruído sal e pimenta porque os pixels desse ruído tem valor máximo ou mínimo
# o que impacta na média calculada, espalhando ele

img = cv2.imread('./imagens/sal_e_pimenta.png')

imgMedia = cv2.blur(img, (7,7)) #mascara usada para média móvel
imgGaussiano = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow('Original', img)
cv2.imshow('Média Móvel', imgMedia)
cv2.imshow('Gaussiano', imgGaussiano)

cv2.waitKey(0)
cv2.destroyAllWindows()