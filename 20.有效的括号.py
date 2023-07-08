#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dic:
                stack.append(char)
            elif len(stack) == 0 or dic[stack.pop()] != char:
                return False
        # if there is element in stack, return false
        return len(stack) == 0


# @lc code=end
