import cv2
import numpy as np

# 4近傍の定義
neiborhood4 = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]],
                        np.uint8)

# 8近傍の定義
neiborhood8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]],
                        np.uint8)

#膨張
def delate(src_img):
    # 8近傍で膨張処理
    for i in range(3):
        src_img = cv2.dilate(src_img,
                              neiborhood8,
                              iterations=1)
#圧縮
def erosion(src_img):
    # 8近傍で縮小処理
    for i in range(3):
        src_img = cv2.erode(src_img,
                              neiborhood8,
                              iterations=1)

#2値化
def binarization2(src_img):
    height, width = src_img.shape[:2]

    #それぞれの色のしきい値
    red_min = 0
    green_min = 80
    blue_min = 0
    red_max = 255
    green_max = 180
    blue_max = 140

    for i in range(height):
        for j in range(width):
            src_img[i, j, 2] = 0 #赤の要素を0
            if src_img[i, j, 0] < blue_min:
                src_img[i, j] = 255 #緑の要素を0
            if src_img[i, j, 0] > blue_max:
                src_img[i, j] = 255 #緑の要素を0
            if src_img[i, j, 1] < green_min:
                src_img[i, j] = 255 #緑の要素を0
            if src_img[i, j, 1] > green_max:
                src_img[i, j] = 255 #緑の要素を0
