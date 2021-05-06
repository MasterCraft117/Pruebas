import cv2

cap = cv2.VideoCapture(1) #0 local o primary camera
con = 0
while cap.isOpened():
    
        #BGR image feed from camera
    ret, img = cap.read()
    #BGR to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img_gray, (11,11), 0, img_gray)
    edges = cv2.Canny(img_gray,10,20,apertureSize = 3)
    
    cv2.imshow("Faces found", edges)
    
    k = cv2.waitKey(10)
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()
