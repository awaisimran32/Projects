import cv2
import numpy as np

img=cv2.imread("used/500.jpg ")
kernel=np.ones((5,5),np.uint8)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img=cv2.GaussianBlur(grayimg,(11,11),0)
img_canny=cv2.Canny(img,100,100)
imgdialation=cv2.dilate(img_canny,kernel,iterations=1)
img_eroded=cv2.erode(imgdialation,kernel,iterations=1)

cv2.imshow("img",img)
cv2.imshow("Gray img",grayimg)
cv2.imshow("blur img",blur_img)
cv2.imshow("canny img",img_canny)
cv2.imshow("dialation img",imgdialation)
cv2.imshow("Eroded img",img_eroded)
cv2.waitKey(0)