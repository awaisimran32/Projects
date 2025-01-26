import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("used/haarcascade_frontalface_default.xml")

path="used/awais3.jpg"
img=cv2.imread(path)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces= faceCascade.detectMultiScale(img_gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("output",img)
cv2.waitKey(0)