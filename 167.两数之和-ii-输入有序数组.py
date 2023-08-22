# @before-stub-for-debug-begin
from python3problem167 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. Hash Table
        # hash_tab = {}
        # for index, val in enumerate(numbers):
        #     remain = target - val
        #     if remain in hash_tab:
        #         return [hash_tab[remain], index + 1]
        #     else:
        #         hash_tab[val] = index + 1

        # 2. Two Pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

# @lc code=end
