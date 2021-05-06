import cv2
import numpy as np

cap = cv2.VideoCapture(0) #0 local o primary camera
con = 0
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceClassif2 = cv2.CascadeClassifier('haarcascade_smile.xml')
faceClassif3 = cv2.CascadeClassifier('haarcascade_eye.xml')
print('¡Bienvenido a la interfaz de OpenCv!')
print('¡Aprende todo lo que puede realizar esta herramienta computacional!')
print('Opciones')
print('1: ')
print('2: Detección de movimiento')
print('3: ')
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
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
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
while cap.isOpened()and decision==3:
    ret, img = cap.read()
    k = cv2.waitKey(10)
    if k==27:
        break
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
