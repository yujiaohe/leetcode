# @before-stub-for-debug-begin
from python3problem189 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k > 0:
            nums[:] = nums[-k:] + nums[:len(nums) - k]


# @lc code=end

