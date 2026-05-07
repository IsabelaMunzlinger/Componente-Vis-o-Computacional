import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


X = [] # Rótulo: o que os dados representam
Y = [] # Características: os dados que representam o rótulo


classes = [0,1] #classes do dataset MNIST


# Caminho imagem
caminho_dataset = './datasets/MNIST/'
#pasta_categoria = '0/'
#nome_imagem = 'mnist_396.png'
#caminho_imagem= os.path.join(caminho_dataset, pasta_categoria, nome_imagem)

for label in classes:
    print(f'Processando a classe {label}...')
    path = os.path.join(caminho_dataset, str(label))

    for img_name in os.listdir(path):
        img = cv2.imread(os.path.join(path, img_name), 0)
        _, binaria = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
        contornos,_ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contornos:
            #objeto = contornos[0]
            objeto = max(contornos, key=cv2.contourArea) #key necessário para indicar que a função max deve usar a área do contorno para comparar os objetos, caso haja mais de um contorno na imagem
            #objeto = max(contornos, key=cv2.contourArea) para pegar o maior contorno, caso haja mais de um
            # Extração de características
            area = cv2.contourArea(objeto)
            perimetro = cv2.arcLength(objeto, True)

            # Armazena dados nos vetores
            X.append([area, perimetro])
            Y.append(label)

# Converte o vetor para o tipo np.array para facilitar o processamento e a manipulação dos dados posteriormente
X = np.array(X)
Y = np.array(Y)

# Separa grupos de teste e de treino
#vetor com as variaveis de treino, X_temp para temporario | 30% temporário e o resto treino
#X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42) #random_state para garantir que a divisão dos dados seja a mesma toda vez que o código for executado, facilitando a reprodução dos resultados
#X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f'Treino: {len(X_train)} | Teste {len(X_test)}')

# Separa o que é zero e um
# quando a posição de Y_train for igual a classe 0, o vetor X_train_0 recebe os dados de X_train correspondentes a essa classe
X_train_0 = X_train[Y_train == classes[0]]
X_train_1 = X_train[Y_train == classes[1]]

# Plotagem dos dados
plt.figure(figsize=(10,6))
plt.scatter(X_train_0[:,0], X_train_0[:,1], c='pink', label=f'Dígito {classes[0]}')
plt.scatter(X_train_1[:,0], X_train_1[:,1], c='blue', label=f'Dígito {classes[1]}') #label é a legenda do gráfico
plt.title(f'Distribuição: Área vs Perímetro (MNIST) {classes[0]} e {classes[1]}')
plt.xlabel('Área')
plt.ylabel('Perímetro')
plt.legend()                                                                                        
plt.grid(True)
plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Pega todos os dados e deixa de 0 a 1
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)

# Cria um espaço com todos os dados de treino, todas as features
knn.fit(X_train_scaled, Y_train)

# Tenta predizer com base no que foi apresentado antes
Y_pred_test = knn.predict(X_test_scaled) 

#Y_test o valor que deveria ter recebido e Y_pred_test o valor que o modelo previu, para comparar os dois e calcular a acurácia do modelo
print(f'Acurácia: {accuracy_score(Y_test, Y_pred_test)}')