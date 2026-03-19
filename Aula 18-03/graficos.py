import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("./Aula 18-03/Imagens/folha_pb.png", cv2.COLOR_BGR2GRAY)

fig, (x1, x2) = plt.subplots(1, 2, figsize=(11, 5))

fig.suptitle('Analise de Imagem')
x1.imshow(imagem)
x1.axis('off')

x2.hist(imagem.ravel(),256,[0,256], color='pink')

plt.tight_layout()
plt.show()