from ast import While
from sre_constants import SUCCESS
import cv2

cap=cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

'''
cap.set(10,100)
'''
while True:
    success, img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break;