import cv2

# A função reduzir_resolucao recebe uma imagem e um fator de redução, e retorna a imagem com resolução reduzida e serrilhada.
def reduzir_resolucao(imagem, fator):
   img_reduzida = imagem[::fator, ::fator]
   img_serrilhada = cv2.resize(img_reduzida, (imagem.shape[1], imagem.shape[0]),interpolation=cv2.INTER_NEAREST)
   cv2.imshow("CV serrilhada", img_serrilhada)
   return img_serrilhada

# Lê a imagem do logo do OpenCV
imagem = cv2.imread("./Aula 25-02/Imagens/OpenCV_Logo.png")
fatores = [2,4,8]

# Laço iterando sobre os fatores de redução, aplicando a função reduzir_resolucao e exibindo os resultados.
for fator in fatores:
   resultado = reduzir_resolucao(imagem, fator)
   cv2.imwrite(f"resultado_fator_{fator}.jpg", resultado)
   cv2.imshow(f"Fator {fator}", resultado)
   cv2.waitKey(0) 