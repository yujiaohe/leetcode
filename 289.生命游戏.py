# @before-stub-for-debug-begin
from python3problem289 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Origin | New | Status
        #    0   |  0  |   0
        #    1   |  0  |   1
        #    0   |  1  |   2
        #    1   |  1  |   3
        ROWS = len(board)
        COLS = len(board[0])

        def neighbourCount(r, c):
            nei = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i == r and j == c) or i < 0 or i >= ROWS or j < 0 or j >= COLS:
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for r in range(ROWS):
            for c in range(COLS):
                nei = neighbourCount(r, c)

                if board[r][c] == 1:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in [2, 3]:
                    board[r][c] = 1
                else:
                    board[r][c] = 0


# @lc code=end
