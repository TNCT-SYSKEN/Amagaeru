import cv2
import numpy as np

if __name__=="__main__":
    img = cv2.imread("item/sample.JPG")
    height, width = img.shape[:2]
    img_copy = img

    #それぞれの色のしきい値
    red_min = 0
    green_min = 80
    blue_min = 0
    red_max = 255
    green_max = 180
    blue_max = 140

    gray_default = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

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

    # 8近傍で膨張処理
    img_dilation = cv2.dilate(img,
                              neiborhood8,
                              iterations=1)
    for i in range(3):
        img_dilation = cv2.dilate(img_dilation,
                              neiborhood8,
                              iterations=1)

    # 8近傍で縮小処理
    img_erosion = cv2.erode(img_dilation,
                              neiborhood8,
                              iterations=1)
    for i in range(3):
        img_erosion = cv2.erode(img_erosion,
                              neiborhood8,
                              iterations=1)

    for i in range(height):
        for j in range(width):
            img_erosion[i, j, 2] = 0 #赤の要素を0
            if img_erosion[i, j, 0] < blue_min:
                img_erosion[i, j] = 255 #緑の要素を0
            if img_erosion[i, j, 0] > blue_max:
                img_erosion[i, j] = 255 #緑の要素を0
            if img_erosion[i, j, 1] < green_min:
                img_erosion[i, j] = 255 #緑の要素を0
            if img_erosion[i, j, 1] > green_max:
                img_erosion[i, j] = 255 #緑の要素を0

    gray = cv2.cvtColor(img_erosion, cv2.COLOR_RGB2GRAY)

    cv2.imshow("src", img_copy)
    cv2.imshow("gray", gray)
    cv2.imwrite("gray.png", gray)
    #cv2.imshow("test", img_erosion)
    cv2.waitKey(0)
