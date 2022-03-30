import cv2
from cv2 import namedWindow

def empty():
    pass

path='resources/lambo.png'

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)

img=cv2.imread(path)

imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Original",img)
cv2.imshow("IMgHSV",imgHSV)
cv2.waitKey(0)