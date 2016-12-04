import cv2
import numpy as np

if __name__=="__main__":
    img = cv2.imread("item/sample.JPG")
    height, width = img.shape[:2]
    img_copy = img

    #それぞれの色のしきい値
    red_min = 0
    green_min = 80
    blue_min = 0
    red_max = 255
    green_max = 180
    blue_max = 140

    gray_default = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    for i in range(height):
        for j in range(width):
            img[i, j, 2] = 0 #赤の要素を0
            if img[i, j, 0] < blue_min:
                img[i, j, 0] = 255 #緑の要素を0
            if img[i, j, 0] > blue_max:
                img[i, j, 0] = 255 #緑の要素を0
            if img[i, j, 1] < green_min:
                img[i, j, 1] = 255 #緑の要素を0
            if img[i, j, 1] > green_max:
                img[i, j, 1] = 255 #緑の要素を0
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imshow("src", img_copy)
    cv2.imshow("gray_default", gray_default)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
