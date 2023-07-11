# @before-stub-for-debug-begin
from python3problem88 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = m - 1, n - 1
        index = m+n-1
        while y >= 0:
            if x >= 0 and nums1[x] >= nums2[y]:
                nums1[index] = nums1[x]
                x -= 1
            else:
                nums1[index] = nums2[y]
                y -= 1
            index -= 1

# @lc code=end
