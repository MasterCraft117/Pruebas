import cv2

cap = cv2.VideoCapture(1) #0 local o primary camera
con = 0
print('¡Bienvenido a la interfaz de OpenCv!')
print('¡Aprende todo lo que puede realizar esta herramienta computacional!')
print('Opciones')
print('')
print('')
decision = int(input("Digite su elección: "))
while ((decision != 0)and(decision != 1)and(decision != 2)and(decision != 3)and(decision != 4)and(decision != 5)):
    decision = int(input("Digite su elección: "))

while cap.isOpened()and decision==1:
    ret, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img_gray, (11,11), 0, img_gray)
    edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
    cv2.imshow("Faces found", edges)
    k = cv2.waitKey(10)
    if k==27:
        break

while cap.isOpened()and decision==2:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==3:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==4:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==5:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break


print('Gracias por utilizar la interfaz de filtros')
cap.release()
cv2.destroyAllWindows()
