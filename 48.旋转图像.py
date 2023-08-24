#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right
            for i in range(right-left):
                tmp = matrix[top][left + i]
                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # move top left into top right
                matrix[top + i][right] = tmp
            left += 1
            right -= 1


# @lc code=end
