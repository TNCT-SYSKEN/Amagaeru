import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__=="__main__":
    imgL = cv2.imread('item/sample.JPG',0)
    imgR = cv2.imread('item/rightside.JPG',0)

    gray_l = cv2.GaussianBlur( cv2.equalizeHist(imgL),(5,5), 0)
    gray_r = cv2.GaussianBlur( cv2.equalizeHist(imgR),(5,5), 0)
    # セミグローバルブロックマッチング
    window_size =5
    minDisp = 32
    numDisp = 144 - minDisp
    stereo = cv2.StereoSGBM_create(
        minDisparity = 0,           # 視差の下限
        numDisparities = 64,        # 最大の上限
        blockSize =15,
        #SADWindowSize = window_size,# SADの窓サイズ
        uniquenessRatio = 10,       # パーセント単位で表現されるマージン
        speckleWindowSize = 0,      # 視差領域の最大サイズ
        speckleRange = 16,          # それぞれの連結成分における最大視差値
        disp12MaxDiff = 0,          # left-right 視差チェックにおけて許容される最大の差
        P1 = 8*3*window_size**2,    # 視差のなめらかさを制御するパラメータ1
        P2 = 32*3*window_size**2,   # 視差のなめらかさを制御するパラメータ2
        #fullDP = False              # 完全な2パス動的計画法を使うならTrue
    )
    disp = stereo.compute(gray_l,gray_r)
    # disp = cv2.normalize(disp, disp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #disparity = stereo.compute(gray_l, gray_r).astype(np.float32)/16
    #disparity = (disparity - minDisp) / numDisp
    cv2.imshow("ShowWindow", disp)
    disparity = stereo.compute(gray_l, gray_r).astype(np.float32)/16
    disparity = (disparity - minDisp) / numDisp
    cv2.imshow("Show window",disparity)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
