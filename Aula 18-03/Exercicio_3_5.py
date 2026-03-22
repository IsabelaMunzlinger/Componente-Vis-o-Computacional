import cv2
import matplotlib.pyplot as plt

# 1. Carrega a imagem em escala de cinza (lembre do 'r' para evitar erro no caminho)
imagem = cv2.imread(r".\Aula 18-03\Imagens\ovelha.png", 0)

# 2. Define os parâmetros manuais
# alpha: Fator de ganho (multiplicação). > 1.0 aumenta o contraste.
# beta: Valor de brilho (soma). > 0 deixa a imagem mais clara.
alpha = 1.2 # Exemplo: 20% a mais de contraste
beta = 30   # Exemplo: soma 30 em todos os pixels (mais brilho)

# 3. Aplica a Transformação Linear (Multiplicação + Soma)
# A fórmula matemática rodando por trás é: pixel_novo = (pixel_antigo * alpha) + beta
# O convertScaleAbs garante que o resultado não passe de 255 nem fique menor que 0.
imagem_linear = cv2.convertScaleAbs(imagem, alpha=alpha, beta=beta)

# 4. Aplica a Equalização Automática Global do OpenCV
imagem_eq = cv2.equalizeHist(imagem)

# 5. Configura a visualização (2 linhas, 3 colunas)
fig, eixos = plt.subplots(2, 3, figsize=(16, 8))
fig.suptitle('Comparativo: Transformação Manual (Linear) vs. Equalização Automática')

imagens = [imagem, imagem_linear, imagem_eq]
titulos = ['Original', f'Manual (Ganho={alpha}, Brilho={beta})', 'Equalização Automática']

for i in range(3):
    # Plota as imagens na primeira linha
    eixos[0, i].imshow(imagens[i], cmap='gray', vmin=0, vmax=255)
    eixos[0, i].set_title(titulos[i])
    eixos[0, i].axis('off')
    
    # Plota os histogramas na segunda linha
    eixos[1, i].hist(imagens[i].ravel(), 256, [0,256], color='pink')
    eixos[1, i].set_title(f"Histograma: {titulos[i]}")
    eixos[1, i].set_xlim([0, 256])

plt.tight_layout()
plt.show()