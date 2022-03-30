import cv2 as cv

img = cv.imread("resources/lena.png")



cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()