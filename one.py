import cv2
import numpy as np

img=cv2.imread("resources/lena.png")
kernel=np.ones((5,5),np.uint8) #matrix of ones with the help of numpy
                                #uint8 = unsigned int 8 bits
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Blur Img",imgBlur)
cv2.imshow("Gray img",imgGray)
cv2.imshow(" img",img)
cv2.imshow(" imgCanny",imgCanny)
cv2.imshow(" imgDialation",imgDialation)
cv2.imshow(" imgEroded",imgEroded)
cv2.waitKey(0)