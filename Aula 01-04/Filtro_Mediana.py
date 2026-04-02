import cv2

img = cv2.imread('./imagens/Noise_SP.png')

#para ruído sal e pimenta funcionou bem porque os ruídos são valores extremos, e a mediana é eficaz para lidar com esses casos, pois ela substitui cada pixel pelo valor mediano dos pixels vizinhos, o que ajuda a eliminar os ruídos sem afetar significativamente as bordas da imagem.
imgTratada = cv2.medianBlur(img,3) #imagem, kernel(5x5)

cv2.imshow('Original', img)
cv2.imshow('Tratada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()