import cv2
import numpy as np

def binarization(src_img, thresh):
    # グレースケールに変換
    if len(src_img.shape) == 3:
        gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = src_img

    # 二値変換
    max_pixel = 100
    ret, img_dst = cv2.threshold(gray_img,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)
    return img_dst
