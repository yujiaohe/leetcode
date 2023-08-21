# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mapping = ['']*numRows
        flag, index = -1, 0
        for char in s:
            mapping[index] += char
            if index == 0 or index == numRows-1:
                flag *= -1
            index += flag
        return ''.join(mapping)


# @lc code=end
