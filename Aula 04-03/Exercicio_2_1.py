import cv2

imagem = cv2.imread("./Aula 04-03/Imagens/cores.png")

b, g, r = cv2.split(imagem)

b = cv2.add(b, 0)
g = cv2.add(g, 0)
r = cv2.add(r, 50)

imagem_unificada = cv2.merge((b,g,r))

cv2.imshow('Cores original', imagem)
cv2.imshow('Cores Claras', imagem_unificada)
cv2.waitKey(0)
cv2.destroyAllWindows()