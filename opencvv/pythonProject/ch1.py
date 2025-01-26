import cv2
import numpy as np
print("import succeeded")
kernel=np.ones((5,5),np.uint8)
#
# img = cv2.imread("used/500.jpg")
# cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Output", 720, 1280)
# cv2.imshow("Output",img)
# cv2.waitKey(0)
cap=cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


while True:
    success,img=cap.read()
    # img_eroded=cv2.erode(imgdialation,kernel,iterations=1)
    cv2.imshow("video",img)
    # cv2.imshow("Eroded img",img_eroded)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break