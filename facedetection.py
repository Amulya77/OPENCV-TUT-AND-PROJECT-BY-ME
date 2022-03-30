import cv2
from cv2 import cvtColor

faceCascade= cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img=cv2.imread('resources/lena.png')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4)


for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result",img)
cv2.waitKey(0)