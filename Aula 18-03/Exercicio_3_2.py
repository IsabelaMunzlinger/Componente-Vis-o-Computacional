import cv2
import matplotlib.pyplot as plt

# 1. Carregar a imagem colorida
imagem_bgr = cv2.imread(r".\Aula 18-03\Imagens\folha_cor.png")

# O OpenCV usa o padrão BGR, mas o Matplotlib usa RGB. 
# Vamos converter a original para RGB apenas para plotar corretamente depois.
imagem_rgb_original = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)

# 2. Separar a imagem nos 3 canais (B, G, R)
b, g, r = cv2.split(imagem_bgr)

# 3. Equalizar cada canal de forma independente
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# 4. Juntar os canais de volta em uma única imagem BGR
imagem_bgr_eq = cv2.merge((b_eq, g_eq, r_eq))

# Converter a equalizada para RGB para plotar
imagem_rgb_eq = cv2.cvtColor(imagem_bgr_eq, cv2.COLOR_BGR2RGB)

# 5. Plotar e comparar
fig, eixos = plt.subplots(1, 2, figsize=(12, 6))

eixos[0].imshow(imagem_rgb_original)
eixos[0].set_title("Imagem Original")
eixos[0].axis('off')

eixos[1].imshow(imagem_rgb_eq)
eixos[1].set_title("Canais Equalizados Separadamente")
eixos[1].axis('off')

plt.tight_layout()
plt.show()