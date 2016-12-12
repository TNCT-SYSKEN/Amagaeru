import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__=="__main__":

    capR = cv2.VideoCapture(1)
    capL = cv2.VideoCapture(2)

    if capR.isOpened() is False:
        raise("IO Error")
    if capL.isOpened() is False:
        raise("IO Error")

    # cv2.namedWindow("CapR", cv2.WINDOW_AUTOSIZE)
    # cv2.namedWindow("CapL", cv2.WINDOW_AUTOSIZE)

    while True:
        ret, imgR = capR.read()
        ret, imgL = capL.read()

        imgGrayL = cv2.GaussianBlur(
                cv2.equalizeHist(
                    cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)),
                (1,1), 0)
        imgGrayR = cv2.GaussianBlur(
                cv2.equalizeHist(
                    cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)),
                (1,1), 0)

        """
        imgGrayR = cv2.GaussianBlur(
                cv2.equalizeHist(
                    cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)),
                (5,5), 0)
        """

        if ret == False:
            continue

        cv2.imshow("Cap1", imgGrayL)
        cv2.imshow("Cap2", imgGrayR)

        k = cv2.waitKey(33)
        # min_disp = 0
        # stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=32, SADWindowSize=21)
        # disparity = stereo.compute(Re_TgtImg_l, Re_TgtImg_r) / 16.0 #画像は8bitのシングルチャンネルの
        """
        stereo = cv2.StereoBM_create(
                cv2.STEREO_BM_BASIC_PRESET,
                ndisparities=int(sys.argv[3]),
                SADWindowSize=int(sys.argv[4]))
        """

        window_size = 10
        minDisp = 32
        numDisp = 144 - minDisp
        stereo = cv2.StereoSGBM_create(
            minDisparity = 0,           # 視差の下限 基本的に0
            numDisparities = 64,        # 最大の上限 16の倍数
            blockSize =13,              # SADWindowSize  SADの窓サイズ 3~13の奇数を推奨
            uniquenessRatio = 0,       # パーセント単位で表現されるマージン
            speckleWindowSize = 0,      # フィルターのサイズ0は使用しない
            speckleRange = 16,          # フィルターの視差の最大値1~2が推奨
            disp12MaxDiff = 0,          # left-right 視差チェックにおけて許容される最大の差
            P1 = 8*3*window_size**2,    # 視差のなめらかさを制御するパラメータ1
            P2 = 32*3*window_size**2,   # 視差のなめらかさを制御するパラメータ2
            #fullDP = False              # 完全な2パス動的計画法を使うならTrue
        )
        # disp = stereo.compute(gray_l,gray_r)
        # disp = stereo.compute(imgGrayL, imgGrayR)
        disp = stereo.compute(imgGrayL, imgGrayR).astype(np.float32)/16
        disp = (disp - minDisp) / numDisp
        cv2.imshow("stereoSGBM", disp)
        # plt.imshow(disp, "gray")
        # plt.show()
        if k == ord('q'):
            break

    cv2.destroyAllWindows()
