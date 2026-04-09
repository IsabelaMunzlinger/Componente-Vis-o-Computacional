#Utilizando o detector de Canny, defina o limiar inferior e superior com valores muito próximos 
# (ex: 100 e 110). Depois, afaste-os (ex: 50 e 200). 
# Relate o que acontece com o ruído de fundo e com a continuidade das bordas 
# principais na imagem lena.png.

# O ruído de fundo é reduzido quando os limites aumentam, porém as bordas ficam um pouco
# mais apagadas. No caso do 50 e 100 o ruído continua mais presente.

import cv2

img = cv2.imread('./imagens/lena.png', 0)

imgTratada = cv2.Canny(img, 100, 110)
imgTratada2 = cv2.Canny(img, 50, 200)

cv2.imshow('Canny - Limiares Próximos', imgTratada)
cv2.imshow('Canny - Limiares Afastados', imgTratada2)

cv2.waitKey(0)
cv2.destroyAllWindows()
