import cv2
import numpy as np
import msvcrt
from contadorobjetos import contadorobjetos

def dibujar(mask,color):
    contornos,__=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        if area > 3000:
            M=cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x=int(M["m10"]/M["m00"])
            y=int(M["m01"]/M["m00"])
            nuevoContorno=cv2.convexHull(c)
            cv2.circle(frame,(x,y),7,(0,255,0),-1)
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
            cv2.drawContours(frame,[nuevoContorno],0,color,3)

cap = cv2.VideoCapture(0) #0 local o primary camera
con = 0
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceClassif2 = cv2.CascadeClassifier('haarcascade_smile.xml')
faceClassif3 = cv2.CascadeClassifier('haarcascade_eye.xml')
print('¡Bienvenido a la interfaz de OpenCv!') #Inicio e impresión de opciones del menú
print('¡Aprende todo lo que puede realizar esta herramienta computacional!')
print('Opciones')
print('1: Detección de figuras')
print('2: Detección de movimiento')
print('3: Contador de objetos')
print('4: Detector Rasgos Faciales')
print('5: Detector de colores')
print('6: Filtro gaussiano, Canny y detección de bordes')
print('0: Salir')
decision = int(input("Digite solamente el número de su elección: ")) #Colocación de un número del 0 al 6

while ((decision != 0)and(decision != 1)and(decision != 2)and(decision != 3)and(decision != 4)and(decision != 5)and(decision != 6)): #Ciclo que evita que se coloquen números desconocidos
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
while cap.isOpened()and decision==2: #Inicio de código de detección de movimiento
            #BGR image feed from camera
    ret, img = cap.read() #Lector de fotogramas
    #BGR to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Conversión a Blanco y Negro

    #Sección de código que lee hasta cierto fotograma con condicionales y coloca contornos identificando el fondo para posteriormente observar el cambio en la pantalla..
    if i == 20:
        bgGray = gray
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 9000: #Definición del área observable
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2) #Impresión de rectángulo que identifica movimiento
    cv2.imshow('Imagen', img) #Impresión de la imagen en tiempo real


    i = i+1 #Suma del contador de fotogramas
    k = cv2.waitKey(10)
    if k==27:
        break #Break del programa
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
    cap=cv2.VideoCapture(0)

    azulBajo=np.array([100,100,20],np.uint8)
    azulAlto=np.array([125,255,255],np.uint8)

    amarilloBajo=np.array([15,100,20],np.uint8)
    amarilloAlto=np.array([45,255,255],np.uint8)

    redBajo1=np.array([0,100,20],np.uint8)
    redAlto1=np.array([5,255,255],np.uint8)

    redBajo2=np.array([175,100,20],np.uint8)
    redAlto2=np.array([179,255,255],np.uint8)

    font=cv2.FONT_HERSHEY_SIMPLEX
    print('Presiona "S" para salir')
    while True:
        ret,frame=cap.read()
        if ret==True:
            frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            maskAzul=cv2.inRange(frameHSV,azulBajo,azulAlto)
            maskAmarillo=cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
            maskRed1=cv2.inRange(frameHSV,redBajo1,redAlto1)
            maskRed2=cv2.inRange(frameHSV,redBajo2,redAlto2)
            maskRed=cv2.add(maskRed1,maskRed2)
            dibujar(maskAzul,(255,0,0))
            dibujar(maskAmarillo,(0,255,255))
            dibujar(maskRed,(0,0,255))
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    break

cap.release()
cv2.destroyAllWindows() #Cierre del proceso de cámara
print("Presione una tecla para cerrar...") #Break funcional a la espera de una tecla
msvcrt.getch()
