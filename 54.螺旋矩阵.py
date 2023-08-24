#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1  # row boundray
        left, right = 0, len(matrix[0]) - 1  # col boundray
        res = []
        while True:
            for i in range(left, right+1):  # ->keep row, col+1
                res.append(matrix[top][i])
            top += 1  # 更新上边界
            if top > bottom:  # 若上边界大于下边界，则遍历遍历完成，下同
                break

            for i in range(top, bottom+1):  # ⬇keep col, row+1
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in range(right, left-1, -1):  # <-keep row, col-1
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            
            for i in range(bottom, top-1, -1):  # ⬆keep col, row-1
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res

# @lc code=end
