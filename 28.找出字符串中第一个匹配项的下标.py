# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # 暴力求解
        # if len(needle) > len(haystack):
        #     return -1
        # for index in range(len(haystack)-len(needle)+1):
        #     if haystack[index:index+len(needle)] == needle:
        #         return index
        # return -1

        # KMP
        # 先计算lps：long prefix sufix
        lps = [0] * len(needle)
        # define 2 pointers, one is the previous LPS
        preLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[preLPS]:
                lps[i] = preLPS + 1
                preLPS += 1
                i += 1
            elif preLPS == 0:
                lps[i] = 0
                i += 1
            else:
                preLPS = lps[preLPS-1]

        i, j = 0, 0  # 2 pointers to haystack, needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return i - len(needle)
        return -1


# @lc code=end
