# -*- coding: utf-8 -*-
import cv2

# マウスイベント時に処理を行う
def mouse_event(event, x, y, flags, param):
    # 左クリックで赤い円形を生成
    if event == cv2.EVENT_MOUSEMOVE:
        print("x:", x, "y:", y, "[R, G, B]", img[y, x])


# 画像の読み込み
img = cv2.imread("item/sample.JPG", 1)
# ウィンドウのサイズを変更可能にする
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# マウスイベント時に関数mouse_eventの処理を行う
cv2.setMouseCallback("img", mouse_event)

# 「Q」が押されるまで画像を表示する
while (True):
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
