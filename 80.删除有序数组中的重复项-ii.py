# @before-stub-for-debug-begin
from python3problem80 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # x, y = 0, 1
        # counter = 1
        # while y < len(nums):
        #     if nums[x] == nums[y]:
        #         if counter < 2:
        #             x += 1
        #             nums[x] = nums[y]
        #         counter += 1
        #     else:
        #         counter = 1
        #         x += 1
        #         nums[x] = nums[y]
        #     y += 1
        # return x + 1

        # 2: 双指针
        # slow: 已处理数组长度，nums[slow-1]为上一个应该保留的元素
        # fast: 已检查数组长度，nums[fast]为即将检查的元素
        # 保留条件：nums[slow-2] != nums[fast]
        n = len(nums)
        if n <= 2:
            return n

        slow, fast = 2, 2
        while fast < len(nums):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        # 3: 用for替代fast
        # slow = 0
        # for num in nums:
        #     # 前面2位直接保留
        #     if slow < 2 or nums[slow-2] != num:
        #         nums[slow] = num
        #         slow += 1
        # return slow


# @lc code=end
