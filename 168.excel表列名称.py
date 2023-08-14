# @before-stub-for-debug-begin
from python3problem168 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            remain = (columnNumber - 1) % 26
            result.append(mapping[remain])
            columnNumber = (columnNumber - 1) // 26
        result.reverse()
        return ''.join(result)



# @lc code=end

