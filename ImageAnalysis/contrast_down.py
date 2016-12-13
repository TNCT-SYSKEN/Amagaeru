# -*- coding: utf-8 -*-

import cv2
import numpy as np
from MouseColor import *
from Binarization import *
from Binarization2 import *

if __name__ == '__main__':
    #コントラストを下げる
    gamma_down =0.2
    #コントラストを上げる
    gamma_up = 8

    # ルックアップテーブルの生成
    look_up_table1 = np.zeros((256, 1), dtype = 'uint8' )
    look_up_table2 = np.zeros((256, 1), dtype = 'uint8' )

    #カラー画像
    img_src = cv2.imread("./item/bright_hu.jpg", 1)
    #コピー
    img = img_src.copy()

    #それぞれの補正値を決める
    for i in range(256):
        look_up_table1[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_down)
        look_up_table2[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma_up)

    #暗い補正
    img_gamma = cv2.LUT(img_src, look_up_table1)
    #明るい補正
    img_gamma = cv2.LUT(img_gamma, look_up_table2)

    #カラーをグレー化
    gray_img = cv2.cvtColor(img_gamma, cv2.COLOR_RGB2GRAY)

    #膨張
    # for i in range(3):
    gray_img = dilate(gray_img)
    #圧縮
    # for i in range(3):
    gray_img = erode(gray_img)
    gray_img = dilate(gray_img)
    gray_img = erode(gray_img)

    #canny法でエッジ検出
    canny_img = cv2.Canny(gray_img, 100, 1000)

    """
    円の検出 対象の画像:canny_img, 変換方法：HOUGH_GRADIENT, param2
    dp ・・・ 処理するときに元画像の解像度を落として検出する場合は増やす。
　　　　　　例えば、1だとそのままの画質で処理して、2だと1/2に縮小して処理するらしい。
    minDist ・・・ 検出される円と円の最小距離
    param1 ・・・ 「Cannyのエッジ検出器で用いる二つのしきい値の高い方」らしい。
    　　　　　　　　　低いほどいろんなエッジを検出する
    param2 ・・・ 中心検出計算時のしきい値。低いほど円じゃないものも検出する
    minRadius ・・・ 最小半径
    maxRadius ・・・ 最大半径
    """
    circles = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT,
                dp=2, minDist=20, param1=20, param2=50,
                minRadius=10, maxRadius=60)

    # imgに検出した円を書き込む
    if circles is not None:
        for (x, y, r) in circles[0]:
            cv2.circle(img, (x, y), r, (255, 255, 255), 1)

    # 表示
    cv2.imshow("canny", canny_img)
    cv2.imshow("gray", gray_img)
    cv2.imshow("img", img)
    # get_mouse_color(img)
    # cv2.imwrite("canny.png", canny_img)
    # cv2.imwrite("people_detection.png", img)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
