# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers
        # 始终移动短板，min(h[left], h[right])才有机会增加
        left, right = 0, len(height) - 1
        drops = 0
        while left < right:
            if height[left] <= height[right]:
                drops = max(drops, height[left]*(right-left))
                left += 1
            else:
                drops = max(drops, height[right]*(right-left))
                right -= 1
        return drops

# @lc code=end
