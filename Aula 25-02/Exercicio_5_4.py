import numpy as np
import cv2

#cria matriz branca de 500x500
matriz_branca = np.ones((500,500), dtype=np.uint8)*255

#slicing para deixar a matriz com listras pretas
matriz_branca[::2,:] = 0

# reduz a matriz pela metade usando slicing
matriz_reduzida = matriz_branca[::2,::2]

cv2.imshow("Matriz Branca", matriz_branca)
cv2.imshow("Matriz Reduzida", matriz_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()