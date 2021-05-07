import cv2
import numpy as np
import msvcrt
from contadorobjetos import contadorobjetos

cap = cv2.VideoCapture(0) #0 local o primary camera
con = 0
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceClassif2 = cv2.CascadeClassifier('haarcascade_smile.xml')
faceClassif3 = cv2.CascadeClassifier('haarcascade_eye.xml')
print('¡Bienvenido a la interfaz de OpenCv!')
print('¡Aprende todo lo que puede realizar esta herramienta computacional!')
print('Opciones')
print('1: Detección de figuras')
print('2: Detección de movimiento')
print('3: Contador de objetos')
print('4: Detector Rasgos Faciales')
print('5: ')
print('6: Filtro gaussiano, Canny y detección de bordes')
print('0: Salir')
decision = int(input("Digite solamente el número de su elección: "))

while ((decision != 0)and(decision != 1)and(decision != 2)and(decision != 3)and(decision != 4)and(decision != 5)and(decision != 6)):
    decision = int(input("Digite su elección: "))
print('Gracias por utilizar la interfaz de filtros')

while cap.isOpened()and decision==6:
    ret, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img_gray, (11,11), 0, img_gray)
    edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
    cv2.imshow("Faces found", edges)
    k = cv2.waitKey(10)
    if k==27:
        break
while cap.isOpened()and decision==1:
    image = cv2.imread('figurasColores2.png')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 10, 150)
    canny = cv2.dilate(canny, None, iterations=1)
    canny = cv2.erode(canny, None, iterations=1)
    #_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(image, cnts, -1, (0,255,0), 2) //Se dibujan los contornos obtenidos

    for c in cnts: #Se dibujan los contornos obtenidos uno por uno
        epsilon = 0.01*cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        #print(len(approx)) #Imprimimos la cantidad de vertices obtenidos en cada uno de los contornos
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx)==3:
            cv2.putText(image, 'Triangulo', (x, y-5),1,1,(0, 255, 0), 1)
            
        if len(approx)==4:
            aspect_ratio = float(w)/h
            #print('aspect_ratio= ', aspect_ratio) #Se compruba la relacion de aspecto
            if aspect_ratio == 1: #Si es de 1 entonces es un rectangulo
                cv2.putText(image, 'Cuadrado', (x, y-5),1,1,(0, 255, 0), 1)
            else:
                cv2.putText(image, 'Rectangulo', (x, y-5),1,1,(0, 255, 0), 1)
        
        if len(approx)==5:
            cv2.putText(image, 'Pentagono', (x, y-5),1,1,(0, 255, 0), 1)
        
        if len(approx)==6:
            cv2.putText(image, 'Hexagono', (x, y-5),1,1,(0, 255, 0), 1)
        
        if len(approx)>10:
            cv2.putText(image, 'Circulo', (x, y-5),1,1,(0, 255, 0), 1)
            
        cv2.drawContours(image, [approx], 0, (0,255,0), 2)
        cv2.imshow('image', image)
        print('Presione una tecla para continuar')
        cv2.waitKey(0) #Se avanza cada que se presione una letra
    break
    
i = 0
while cap.isOpened()and decision==2:
            #BGR image feed from camera
    ret, img = cap.read()
    #BGR to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    if i == 20:
        bgGray = gray
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 9000:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
    cv2.imshow('Imagen', img)


    i = i+1
    k = cv2.waitKey(10)
    if k==27:
        break
if decision==3:
    contadorobjetos()

while cap.isOpened()and decision==4:
    ret, img = cap.read()
    img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(img_gray, 1.3, 5)
    smile=faceClassif2.detectMultiScale(img_gray, 1.3, 5)
    eye=faceClassif3.detectMultiScale(img_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
    for (x,y,w,h) in smile:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
    for (x,y,w,h) in eye:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
    if not ret:
        break
    if img is None:
        break
    cv2.imshow("Reconocimiento_Facial", img)
    k = cv2.waitKey(10)
    if k==27:
        break

while cap.isOpened()and decision==5:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
print("Presione una tecla para cerrar...")
#msvcrt.getch()
