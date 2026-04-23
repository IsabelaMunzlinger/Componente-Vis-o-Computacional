#Desenvolva um algoritmo que processe o arquivo de vídeo objetos-coloridos.mov e realize o 
# rastreamento em tempo real de cada objeto que cruza a tela. Imprima na imagem o centroide do objeto. 
# Ajuste a velocidade do video para que possa ser lida as mensagens.

import cv2
import numpy as np

cap = cv2.VideoCapture('./Aula 22-04/videos/objetos-coloridos.mov')

