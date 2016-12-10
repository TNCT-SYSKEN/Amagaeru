import cv2
import numpy as np


if __name__=='__main__':

    img_src = cv2.imread("./item/DSC00248.JPG",1)
    #基準
    img_adj = cv2.imread("./item/sample.JPG",1)

    ave1 = np.average(img_src)
    ave2 = np.average(img_adj)


    gamma = ave2/ave1
    look_up_table = np.ones((256,1), dtype='uint8')*0

    for i in range(256):
        look_up_table[i][0]=255*pow(float(i)/255, 1.0/abs(gamma))

    #変換
    img_gamma = cv2.LUT(img_src, look_up_table)
    #output
    cv2.imshow("Show window",img_gamma)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
