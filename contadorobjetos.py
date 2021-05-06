# Programa de deteccion de objetos por contorno y contador.
# Rogelio Guzman Cruzado
# Referencia: https://www.youtube.com/watch?v=jYSdkLBzD88&ab_channel=OMES

import cv2

img = cv2.imread()
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale, 100, 200)

cntours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, cntours, -1, (0, 0, 255), 2)

cv2.imshow('edges', edges)
cv2.imshow('edges', edges)
cv2.waitkey(0)
cv2.destroyAllWindows
