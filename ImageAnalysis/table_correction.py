# 補正データを格納
import sys

"""
円のフィルター
ある座席に検出されるであろう場所と大きさでフィルターを無理やりかける
"""
table_correction = [[0 for i in range(8)] for j in range(6)]

table_correction[0][0] = (0, 0, 0)
table_correction[0][1] = (727, 65, 25)
table_correction[0][2] = (0, 0, 0)
table_correction[0][3] = (0, 0, 0)
table_correction[0][4] = (0, 0, 0)
table_correction[0][5] = (0, 0, 0)
table_correction[0][6] = (0, 0, 0)
table_correction[0][7] = (0, 0, 0)

table_correction[1][0] = (0, 0, 0)
table_correction[1][1] = (0, 0, 0)
table_correction[1][2] = (0, 0, 0)
table_correction[1][3] = (0, 0, 0)
table_correction[1][4] = (957, 259, 30)
table_correction[1][5] = (0, 0, 0)
table_correction[1][6] = (0, 0, 0)
table_correction[1][7] = (930, 730, 60)

table_correction[2][0] = (1143, 37, 17)
table_correction[2][1] = (0, 0 ,0)
table_correction[2][2] = (1195, 91, 20)
table_correction[2][3] = (0, 0, 0)
table_correction[2][4] = (0, 0, 0)
table_correction[2][5] = (0, 0, 0)
table_correction[2][6] = (1485, 477, 50)
table_correction[2][7] = (0, 0, 0)

table_correction[3][0] = (0, 0, 0)
table_correction[3][1] = (0, 0, 0)
table_correction[3][2] = (0, 0, 0)
table_correction[3][3] = (0, 0, 0)
table_correction[3][4] = (0, 0, 0)
table_correction[3][5] = (0, 0, 0)
table_correction[3][6] = (0, 0, 0)
table_correction[3][7] = (0, 0, 0)

table_correction[4][0] = (0, 0, 0)
table_correction[4][1] = (0, 0, 0)
table_correction[4][2] = (0, 0, 0)
table_correction[4][3] = (0, 0, 0)
table_correction[4][4] = (0, 0, 0)
table_correction[4][5] = (0, 0, 0)
table_correction[4][6] = (0, 0, 0)
table_correction[4][7] = (0, 0, 0)

table_correction[5][0] = (0, 0, 0)
table_correction[5][1] = (0, 0, 0)
table_correction[5][2] = (0, 0, 0)
table_correction[5][3] = (0, 0, 0)
table_correction[5][4] = (0, 0, 0)
table_correction[5][5] = (0, 0, 0)
table_correction[5][6] = (0, 0, 0)
table_correction[5][7] = (0, 0, 0)
