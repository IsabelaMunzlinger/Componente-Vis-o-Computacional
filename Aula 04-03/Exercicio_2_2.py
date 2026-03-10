import cv2

imagem = cv2.imread("./Aula 04-03/Imagens/frutas.png")

imagem_escura = cv2.subtract(imagem, (150,150,150,0))

b_original, g_original, r_original = cv2.split(imagem)
b_escuro, g_escuro, r_escuro = cv2.split(imagem_escura)

limiar = 120
#Significa que se o valor do pixel for menor que 120, ele vira preto, se for maior, vira branco
_, segmento_original = cv2.threshold(b_original, limiar, 255, cv2.THRESH_BINARY) #thresholding, ou seja, segmentação por limiarização
_, segmento_escuro = cv2.threshold(b_escuro, limiar, 255, cv2.THRESH_BINARY) #segmento_escuro é a imagem segmentada da imagem escura


cv2.imshow('Frutas', segmento_original)
cv2.waitKey(0)
cv2.imshow('Frutas Escuras', segmento_escuro)
cv2.waitKey(0)

##A questão pergunta: "Por que o mesmo valor de corte não funciona para as duas matrizes?"

# A resposta que se espera de você:A limiarização depende da intensidade dos pixels. 
# Quando você subtrai 150 de cada pixel, você desloca o histograma da imagem para a esquerda (para o preto).Se na imagem original um objeto verde tinha intensidade 180 e seu corte era 120, ele seria segmentado (180 > 120).
# Na imagem escurecida, esse mesmo objeto passou a ter intensidade 30 ($180 - 150 = 30$). Como 30 é menor 
# que o corte de 120, o objeto "desaparece" da segmentação ou fica fundido ao fundo.