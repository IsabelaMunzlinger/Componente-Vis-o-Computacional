import cv2
import numpy as np

frutas = cv2.imread('./Imagens/frutas.png')
frutas_escuras = cv2.imread('./Imagens/frutas_escuras.png')
frutas_claras = cv2.imread('./Imagens/frutas_claras.png')

hsvFrutas = cv2.cvtColor(frutas, cv2.COLOR_BGR2HSV) #converte de rgb para hsv
hsvFrutasEscuras = cv2.cvtColor(frutas_escuras, cv2.COLOR_BGR2HSV)
hsvFrutasClaras = cv2.cvtColor(frutas_claras, cv2.COLOR_BGR2HSV)

print(hsvFrutas.shape)

h_clara, _, _ = cv2.split(hsvFrutasClaras) #precisa de 3 retornos por isso usa uma tupla
h_original, _, _ = cv2.split(hsvFrutas) #por padrão coloca underline quando não usa 
h_escura, _, _ = cv2.split(hsvFrutasEscuras)

h_visual_clara = cv2.applyColorMap(h_clara, cv2.COLORMAP_JET) #aplica um mapa de cores para melhor visualização
h_visual_original = cv2.applyColorMap(h_original, cv2.COLORMAP_JET)
h_visual_escura = cv2.applyColorMap(h_escura, cv2.COLORMAP_JET)

#Máscara aplicada para destacar cores
cv2.imshow('H Clara', h_visual_clara)
cv2.imshow('H Original', h_visual_original)
cv2.imshow('H Escura', h_visual_escura)

cv2.waitKey(0)
cv2.destroyAllWindows()