import cv2
import numpy as np

img = cv2.imread("used/500.jpg")
imgresize=cv2.resize(img,(300,200))
imgcropped=img[0:200,200:500]


print(img.shape)
cv2.imshow("Image",img)
cv2.imshow("Image resize",imgresize)
cv2.imshow("Image cropped",imgcropped)

cv2.waitKey(0)