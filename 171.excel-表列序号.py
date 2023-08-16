# @before-stub-for-debug-begin
from python3problem171 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ord('A') = 65, ord('Z') = 90
        result = 0
        for char in columnTitle:
            result = result * 26 + ord(char) - ord('A') + 1
        return result


# @lc code=end
