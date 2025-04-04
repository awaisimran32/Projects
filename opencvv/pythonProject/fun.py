import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier("used/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("used/haarcascade_eye.xml")
kernel=np.ones((5,5),np.uint8)

cap=cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


while True:
    success,img=cap.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img_gray, 1.1, 4)
    eyes = smileCascade.detectMultiScale(img_gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    if not success:
        print("Cannot Capture.")
        break
    cv2.imshow("video",img)
    # cv2.imshow("gray video",img_gray)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break









