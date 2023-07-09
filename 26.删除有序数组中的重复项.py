# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # default: len(nums) >= 1
        x, y = 0, 1
        while y < len(nums):
            if nums[x] == nums[y]:
                y += 1
            else:
                nums[x+1], nums[y] = nums[y], nums[x+1]
                x += 1
                y += 1
        return x+1


# @lc code=end
