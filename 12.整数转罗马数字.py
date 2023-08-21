# @before-stub-for-debug-begin
from python3problem12 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                   90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                   9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ''
        while num:
            for key, value in mapping.items():
                cnt = num // key
                num %= key
                result += value * cnt
        return result


# @lc code=end
