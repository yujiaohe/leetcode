# @before-stub-for-debug-begin
from python3problem392 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Tow Pointers
        if len(s) > len(t):
            return False
        x, y = 0, 0
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x, y = x + 1, y + 1
            else:
                y += 1
        return x == len(s)

# @lc code=end
