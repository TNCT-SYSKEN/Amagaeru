# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    gamma =0.25

    # ルックアップテーブルの生成
    look_up_table = np.zeros((256, 1), dtype = 'uint8' )

    for i in range(256):
        look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

    # 画像の読み込み
    img_src = cv2.imread("./item/bright_hu.jpg", 1)

    # 補正
    img_gamma = cv2.LUT(img_src, look_up_table)

    # 画像の保存
    cv2.imwrite('./item/dark_hu.jpg', img_gamma)

    # 表示
    #cv2.imshow("Show LOW CONTRAST Image", img_gamma)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
