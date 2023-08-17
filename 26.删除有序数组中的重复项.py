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
        # 双指针
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[slow-1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow



# @lc code=end
