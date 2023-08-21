# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers
        left, right = 0, len(s) - 1
        stack = []
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

# @lc code=end
