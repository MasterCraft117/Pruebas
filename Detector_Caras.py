import cv2
import time
import argparse


if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"])
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while cap.isOpened():
        
        success,img = cap.read()
        img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceClassif.detectMultiScale(img_gray, 1.3, 5)
        for (x,y,w,h) in faces:
             cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        if not success:
            break
        if img is None:
            break

        
        cv2.imshow("Reconocimiento_Facial", img)

        k = cv2.waitKey(10)
        if k==27:
            break


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))



