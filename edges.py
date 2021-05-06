import cv2

cap = cv2.VideoCapture(0) #0 local o primary camera
con = 0
while cap.isOpened():
    
        # Feed de la camara.
    ret, img = cap.read()
    # Convierte la imagen a escala de grises.
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Agrega blur gaussiano.
    cv2.GaussianBlur(img_gray, (11,11), 0, img_gray)
    # Funcion de deteccion de bordes.
    edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
    
    cv2.imshow("Deteccion de bordes", edges)
    
    k = cv2.waitKey(10)
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()
