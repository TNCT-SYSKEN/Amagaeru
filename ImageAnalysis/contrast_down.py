# -*- coding: utf-8 -*-

import cv2
import numpy as np
from Binarization import *
from Binarization2 import *

if __name__ == '__main__':
    gamma_down =0.25
    gamma_up = 8

    # ルックアップテーブルの生成
    look_up_table1 = np.zeros((256, 1), dtype = 'uint8' )
    look_up_table2 = np.zeros((256, 1), dtype = 'uint8' )

    img_src = cv2.imread("./item/bright_hu.jpg", 1)

    #暗い補正
    for i in range(256):
        look_up_table1[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_down)
        look_up_table2[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_up)
    img_gamma = cv2.LUT(img_src, look_up_table1)
    img_gamma = cv2.LUT(img_gamma, look_up_table2)

    gray_img = cv2.cvtColor(img_gamma, cv2.COLOR_RGB2GRAY)
    #canny法
    canny_img = cv2.Canny(gray_img, 100, 1000)

    circles = cv2.HoughCircles(img_gamma,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
    # 表示
    cv2.imshow("Show LOW CONTRAST I", img_gamma)
    cv2.imshow("Show LOW CONTRAST Image", canny_img)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
