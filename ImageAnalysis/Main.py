import cv2
import numpy as np

from MouseColor import *

if __name__=="__main__":
    src_img = cv2.imread("item/sample.JPG")

    #マウスの座標のRGBを取得
    #get_mouse_color(src_img)

    cv2.imshow("src", src_img)
    #cv2.imshow("dst", dst_img)
    cv2.waitKey(0)
