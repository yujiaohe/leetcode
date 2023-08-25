# @before-stub-for-debug-begin
from python3problem383 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount, magCount = {}, {}
        for c in ransomNote:
            ransomCount[c] = ransomCount.get(c, 0) + 1

        for c in magazine:
            magCount[c] = magCount.get(c, 0) + 1

        for key in ransomCount:
            if key not in magCount or ransomCount[key] > magCount[key]:
                return False
        return True

# @lc code=end
