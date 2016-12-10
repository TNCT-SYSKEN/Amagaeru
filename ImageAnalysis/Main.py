import cv2
import numpy as np

from MouseColor import *
from Binarization import *
from Binarization2 import *
from Compression import *

if __name__=="__main__":
    src_img = cv2.imread("item/sample.JPG")

    # 標準の2値化(カラー画像としきい値を渡す)
    # src_img = binarization(src_img, 100)

    #マウスの座標のRGBを取得
    get_mouse_color(src_img)

    cv2.imshow("src", src_img)
    #cv2.imshow("dst", dst_img)
    cv2.waitKey(0)
