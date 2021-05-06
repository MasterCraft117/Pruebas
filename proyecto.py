import cv2

cap = cv2.VideoCapture(1) #0 local o primary camera
con = 0
print('¡Bienvenido a la interfaz de OpenCv!')
print('¡Aprende todo lo que puede realizar esta herramienta computacional!')
print('Opciones')
print('1: ')
print('2: Detección de movimiento')
print('3: ')
print('4: ')
print('5: ')
print('6: Filtro gaussiano, Canny y detección de bordes')
print('0: Salir')
decision = int(input("Digite solamente el número de su elección: "))
while ((decision != 0)and(decision != 1)and(decision != 2)and(decision != 3)and(decision != 4)and(decision != 5)(decision != 6)):
    decision = int(input("Digite su elección: "))

while cap.isOpened()and decision==6:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img_gray, (11,11), 0, img_gray)
    edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
    cv2.imshow("Faces found", edges)
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==1:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==2:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==3:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==4:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==5:
    print('Gracias por utilizar la interfaz de filtros')
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
print('Gracias por utilizar la interfaz de filtros')
cap.release()
cv2.destroyAllWindows()
