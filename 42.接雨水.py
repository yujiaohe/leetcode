# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # maxL, maxR = [0]*n, [0]*n  # record the max height from left and right
        # result = 0
        # for index in range(1, n):
        #     maxL[index] = max(maxL[index-1], height[index-1])

        # for index in range(n-2, -1, -1):
        #     maxR[index] = max(maxR[index+1], height[index+1])

        # for index in range(n):
        #     min_h = min(maxL[index], maxR[index])
        #     # min height of left and right > current height
        #     if min_h - height[index] > 0:
        #         result += min_h - height[index]
        # return result
    
        # 2 pointers
        pointerL, pointerR = 0, len(height) - 1
        maxL, maxR = 0, 0
        result = 0
        while pointerL <= pointerR:
            if maxL <= maxR:
                result += max(0, maxL - height[pointerL])
                maxL = max(maxL, height[pointerL])
                pointerL += 1
            else:
                result += max(0, maxR - height[pointerR])
                maxR = max(maxR, height[pointerR])
                pointerR -= 1
        return result


# @lc code=end
