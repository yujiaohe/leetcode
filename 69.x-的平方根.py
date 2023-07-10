#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # for num in range(0, max(1, math.ceil(x/2) + 1)):
        #     left = num * num
        #     right = (num + 1) * (num + 1)
        #     if x >= left and x < right:
        #         return num
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            # mid = (left + right) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1


# @lc code=end
