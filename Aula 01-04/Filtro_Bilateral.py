import cv2

#Funciona bem com o ruído gaussiano, mas não é tão eficaz para o ruído de sal e pimenta. Ele preserva as bordas, o que é uma vantagem em comparação com outros filtros, mas pode ser mais lento devido à sua complexidade computacional.

img = cv2.imread('./imagens/Noise_SP.png', 0)

imgTratada = cv2.bilateralFilter(img, 15,131,31) #imagem, raio, sigmaColor(filtra cores próximas), sigmaSpace(filtra de acordo com a distancia)
#para imagens estáticas não recomenda passar de 9 o raio, e vídeo 5

cv2.imshow('Original', img)
cv2.imshow('Tratada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()