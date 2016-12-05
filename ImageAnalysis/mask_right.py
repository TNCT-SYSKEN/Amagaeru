import cv2
import numpy as np

if __name__=='__main__':
    #画像の読み込み
    img_src = cv2.imread("./image/DSC00248.JPG",1)

    #マスクの読み込み
    img_mask = cv2.imread("./image/mask_right.png",0)
    #マスクの適応
    img_masked = cv2.bitwise_and(img_src, img_src, mask=img_mask)

    cv2.imshow("Show MASK Image",img_masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
