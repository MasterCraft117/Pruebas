import cv2

cap = cv2.VideoCapture(1) #0 local o primary camera
con = 0
i = 0
while cap.isOpened():
    
        #BGR image feed from camera
    ret, img = cap.read()
    #BGR to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Faces found", gray)

    if i == 20:
        bgGray = gray
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        cv2.imshow('dif', dif)
                   
    i = i+1
    
    k = cv2.waitKey(10)
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()
