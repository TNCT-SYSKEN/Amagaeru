import cv2
import numpy as np

if __name__=="__main__":
    img = cv2.imread("item/sample.JPG")
    height, width = img.shape[:2]

    gray_from_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #青は絶対0かな
    for i in range(height):
        for j in range(width):
            img[i, j, 0] = 0 #青の要素を0
            img[i, j, 2] = 0 #緑の要素を0

    gray_from_img_green = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    canny1 = cv2.Canny(gray_from_img_green, 50, 110)
    canny2 = cv2.Canny(gray_from_img, 50, 110)

    #img_tmp = cv2.Sobel(gray_img, cv2.CV_32F, 1, 0)

    cv2.namedWindow("sample")
    cv2.imshow("sample", img)
    cv2.imshow("sample1", canny1)
    cv2.imshow("sample2", canny2)
    cv2.waitKey(0)