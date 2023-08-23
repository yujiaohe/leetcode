# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window
        start, total = 0, 0
        result = float('inf')
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                result = min(result, end - start + 1)
                total -= nums[start]
                start += 1
        return 0 if result == float('inf') else result

# @lc code=end
