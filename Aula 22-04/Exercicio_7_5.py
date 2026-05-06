# Crie um sistema de inspeção de peças. O algoritmo deve analisar as imagens 
# parafusos1.png, parafusos2.png e parafusos3.png. 
# O sistema deve desenhar um quadrado verde sobre as peças com apenas um furo com a 
# escrita "OK" e um retangulo vermelho 
# com a escrita "Defeito" sobra as peças sem furo ou com mais de um furo.
import cv2
import numpy as np

img = cv2.imread("./imagens/parafusos1.png")

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_cinza = cv2.GaussianBlur(img_cinza, (15,15), 0)

sobelx_64 = cv2.Sobel(img_cinza, cv2.CV_8U, 1, 0, ksize=3)
sobely_64 = cv2.Sobel(img_cinza, cv2.CV_8U, 0, 1, ksize=3)

sobelx = cv2.convertScaleAbs(sobelx_64)
sobely = cv2.convertScaleAbs(sobely_64)

sobelCombinado = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)


sobelCombinado = cv2.add(img_cinza, sobelCombinado)

metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

ret, imgBinarizada = cv2.threshold(img_cinza, 200, 255, metodo) 

imgAdaptativa = cv2.adaptiveThreshold(sobelCombinado, 255, 
                                      cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY_INV, 31, 5)

thresh = cv2.add(imgAdaptativa, imgBinarizada)

contornos, hierarquia = cv2.findContours(
    thresh,
    cv2.RETR_CCOMP,
    cv2.CHAIN_APPROX_SIMPLE
)

hierarquia = hierarquia[0]
img_saida = img.copy()

areas = [cv2.contourArea(c) for c in contornos]

for i in range(len(contornos)):

    if hierarquia[i][-1] == -1:

        area_peca = areas[i]

        if area_peca < 1000:
            continue

        x, y, w, h = cv2.boundingRect(contornos[i])

        qtd_furos = 0

        for j in range(len(contornos)):
            if hierarquia[j][-1] == i:

                area_furo = areas[j]

                # filtra ruído de furo
                if area_furo > 50 and area_furo < area_peca * 0.8:
                    qtd_furos += 1

        if qtd_furos == 1:
            cor = (0, 255, 0)
            texto = "OK"
        else:
            cor = (0, 0, 255)
            texto = "Defeito"

        cv2.rectangle(img_saida, (x, y), (x + w, y + h), cor, 2)
        cv2.putText(img_saida, texto, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)
        
# resultado final
cv2.imshow("Resultado", img_saida)
cv2.imshow("thresh", thresh)
cv2.imshow("cinza filtrado", img_cinza)


cv2.waitKey(0)
cv2.destroyAllWindows()