# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        # 斐波那契数列
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, (a+b)
        return b


# @lc code=end
