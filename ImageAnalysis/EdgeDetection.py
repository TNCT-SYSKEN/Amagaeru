import cv2
import numpy as np

if __name__=="__main__":
    #cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    img = cv2.imread("item/sample.JPG")

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    laplacian = gray_img
    #cv2.Laplacian(gray_img, laplacian, CV_32F)
	#cv2.convertScaleAbs(laplacian, laplacian)

    img_tmp = cv2.Sobel(gray_img, cv2.CV_32F, 1, 0)

    canny_img = cv2.Canny(gray_img, 50, 110)

    cv2.namedWindow("sample")
    cv2.imshow("canny", canny_img)
    cv2.imshow("sample", img)
    cv2.waitKey(0)
