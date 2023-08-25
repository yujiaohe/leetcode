# @before-stub-for-debug-begin
from python3problem73 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. O(m*n)
        # import copy
        # copy_matrix = copy.deepcopy(matrix)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             for i in range(COLS):
        #                 copy_matrix[r][i] = 0
        #             for i in range(ROWS):
        #                 copy_matrix[i][c] = 0
        # for r in range(ROWS):
        # matrix[r] = copy_matrix[r]

        # 2. O(m+n)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # row_flag = [0]*ROWS
        # col_flag = [0]*COLS
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             row_flag[r] = 1
        #             col_flag[c] = 1

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if row_flag[r] or col_flag[c]:
        #             matrix[r][c] = 0

        # 3. O(1)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False

        # determine which row, col need to be set to 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # matrix[0] for col flag

                    if r == 0:  # rowZero for first row flag
                        rowZero = True
                    else:
                        matrix[r][0] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # special management of first col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # specila management of first row (this need after 1st col check)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


# @lc code=end
