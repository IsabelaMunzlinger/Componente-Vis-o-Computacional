import cv2

imagem = cv2.imread("./Aula 25-02/Imagens/windows_xp.jpg")

k = 8
intervalo = 256//k

img_quatizada = (imagem//intervalo)*intervalo

print(type(intervalo))
print(str(intervalo))

cv2.imshow("Windows XP", imagem)
cv2.imshow("Windows XP Quatizada", img_quatizada)
cv2.waitKey(0)
cv2.destroyAllWindows()