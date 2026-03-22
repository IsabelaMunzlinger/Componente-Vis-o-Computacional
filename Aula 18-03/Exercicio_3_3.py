import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread(r".\Aula 18-03\Imagens\folha_cor.png")

# 1. Converte de BGR para HSV
hsvFolha = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) 

# 2. Separa os canais da imagem HSV (Ajustado)
h, s, v = cv2.split(hsvFolha) 

# 3. Equaliza direto o canal V (Removido o .ravel())
v_eq = cv2.equalizeHist(v)

# 4. Junta os canais novamente
imagem_hsv = cv2.merge((h, s, v_eq))

# 5. Retorna para BGR
imagemBGR = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

# 6. Imprime na tela
cv2.imshow('Canal v equalizado', imagemBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()