import cv2
import numpy as np

img = cv2.imread('item/bright_hu.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
            dp=2, minDist=20, param1=20, param2=110,
            minRadius=30, maxRadius=70)

# Draw detected circles on the original image.
if circles is not None:
    for (x, y, r) in circles[0]:
        cv2.circle(img, (x, y), r, (0, 0, 255), 1)

cv2.imshow('detected circles',cimg)
cv2.imshow('detected cir',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
