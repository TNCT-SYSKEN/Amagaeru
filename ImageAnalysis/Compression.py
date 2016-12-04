import cv2
import numpy as np

if __name__=="__main__":
    img = cv2.imread("item/sample.JPG")
    height, width = img.shape[:2]
    size = ((int)(width/2), (int)(height/2))

    resize = cv2.resize(img, size)

    cv2.namedWindow("src")
    cv2.namedWindow("sample")
    cv2.imshow("src", img)
    cv2.imshow("sample", resize)
    cv2.waitKey(0)
    cv2.destroyWindow("sample")
    cv2.destroyWindow("src")
