# @before-stub-for-debug-begin
from python3problem27 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for num in nums:
            if num != val:
                nums[x] = num
                x += 1
        return x

# @lc code=end
