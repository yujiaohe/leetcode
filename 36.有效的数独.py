# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # reversed = list(zip(*board))
        # box = []
        # for _ in range(len(board)):
        #     box.append([])

        # # generate box
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         index = (row // 3) * 3 + col // 3
        #         box[index].append(board[row][col])

        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         char = board[row][col]
        #         if char != '.':
        #             index = (row // 3) * 3 + col // 3
        #             # row, col, 3*3 box check
        #             if board[row].count(char) > 1 or reversed[col].count(char) > 1 or box[index].count(char) > 1:
        #                 return False

        # return True
    

        # HashSet 
        rows, cols, box = [], [], []
        for _ in range(len(board)):
            rows.append([0]*9)
            cols.append([0]*9)
            box.append([0]*9)

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char != '.':
                    num = int(char) - 1
                    index = (i // 3) * 3 + j // 3
                    rows[i][num] += 1
                    cols[j][num] += 1
                    box[index][num] += 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or box[index][num] > 1:
                        return False
        return True


# @lc code=end
