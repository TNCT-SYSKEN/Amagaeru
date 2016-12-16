# -*- coding: utf-8 -*-

import cv2
import numpy as np
from Binarization import *
from Binarization2 import *
from MouseColor import *

def under(val):
    if val < 0:
        val = 0
    return val

if __name__ == '__main__':
    gamma_down =0.25
    gamma_up = 8


    # ルックアップテーブルの生成
    look_up_table1 = np.zeros((256, 1), dtype = 'uint8' )
    look_up_table2 = np.zeros((256, 1), dtype = 'uint8' )

    img_src = cv2.imread("./item/bright_hu.jpg", 1)
    img = img_src.copy()

    # get_mouse_color(img)
    # img[:,:] -= [70, 110, 170]
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            if ((img.item(i, j, 0) < 100) & (img.item(i, j, 1) < 100) & (img.item(i, j, 2) < 100)):
                img.itemset((i, j, 0), 255)
                img.itemset((i, j, 1), 255)
                img.itemset((i, j, 2), 255)
            """
            else:
                img.itemset((i, j, 0), under(img.item(i, j, 0) - 100))
                img.itemset((i, j, 1), under(img.item(i, j, 1) - 130))
                img.itemset((i, j, 2), under(img.item(i, j, 2) - 200))
            """
    # get_mouse_color(img)

    #暗い補正
    for i in range(256):
        look_up_table1[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_down)
        look_up_table2[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_up)
    img_gamma = cv2.LUT(img_src, look_up_table1)
    img_gamma = cv2.LUT(img_gamma, look_up_table2)

    gray_img = cv2.cvtColor(img_gamma, cv2.COLOR_RGB2GRAY)
    #canny法
    canny_img = cv2.Canny(gray_img, 100, 1000)

    circles = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT,
                dp=2, minDist=20, param1=20, param2=50,
                minRadius=10, maxRadius=60)

    # Draw detected circles on the original image.
    """
    if circles is not None:
        for (x, y, r) in circles[0]:
            cv2.circle(img, (x, y), r, (255, 255, 255), 1)
    """

    # 表示
    cv2.imshow("canny", canny_img)
    cv2.imshow("people detection", img)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
