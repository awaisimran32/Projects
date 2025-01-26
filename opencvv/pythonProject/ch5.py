import cv2
import numpy as np

img= cv2.imread("used/card.jpg")
width,height=250,350
pt1= np.float32([[948,209],[1244,330],[732,571],[1095,774]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgout=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("image",img)
cv2.imshow("image1",imgout)
cv2.waitKey(0)
