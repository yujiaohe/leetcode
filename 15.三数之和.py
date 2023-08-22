# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    three_sum = val + nums[left] + nums[right]
                    if three_sum < 0:
                        left += 1
                    elif three_sum > 0:
                        right -= 1
                    else:
                        result.append([val, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

        return result


# @lc code=end
