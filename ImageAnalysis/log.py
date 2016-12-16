import cv2
import math
import numpy as np

gamma = 0.1

lookUpTable = np.zeros((256, 1), dtype = 'uint8')

#明るくする
for i in range(256):
	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

img_src = cv2.imread('item/sample.JPG', 1)
img_gamma = cv2.LUT(img_src, lookUpTable)
height, width = img_src.shape[:2]

for i in range(height):
    for j in range(width):
        img_gamma[i, j, 0] = 0 #青の要素を0

img_gray = cv2.cvtColor(img_gamma, cv2.COLOR_BGR2GRAY)
# 二値変換
thresh = 10
max_pixel = 255
ret, img_dst = cv2.threshold(img_gray,
                             thresh,
                             max_pixel,
                             cv2.THRESH_BINARY)

cv2.imshow('src', img_src)
cv2.imshow('lutImage', img_dst)
cv2.waitKey()
