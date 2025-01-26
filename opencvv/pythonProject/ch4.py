import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[:]=120,45,30
cv2.line(img,(0,0),(300,300),(0,255,0),5 )
cv2.rectangle(img,(0,0),(250,200),(0,0,255),5 ,cv2.FILLED)
cv2.circle(img,(100,50),100,(200,100,0),5,cv2.FILLED)
cv2.putText(img,"opencv task",(200,320),cv2.FONT_HERSHEY_PLAIN,3,(0,150,0))

cv2.imshow("Image",img)

cv2.waitKey(0)