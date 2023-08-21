# @before-stub-for-debug-begin
from python3problem151 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.strip().split()
        strs.reverse()
        return ' '.join(strs)
# @lc code=end

