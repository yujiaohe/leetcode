# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        for val in digits[::-1]:
            result.append((val + carry) % 10)
            carry = (val + carry) // 10
        result = result[::-1]
        return [carry] + result if carry else result
# @lc code=end
