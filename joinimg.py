import cv2
import numpy as np

img=cv2.imread("resources/lena.png")


hor=np.hstack((img,img))
ver=np.vstack((img,img))

cv2.imshow("horizontal",hor)
cv2.imshow("VeERTICAL",ver)

cv2.waitKey(0)