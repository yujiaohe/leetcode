# @before-stub-for-debug-begin
from python3problem101 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isEqual(left, right):
            if left and right:
                return left.val == right.val and isEqual(left.left, right.right) and isEqual(left.right, right.left)
            elif not left and not right:
                return True
            else:
                return False
            
        if root:
            return isEqual(root.left, root.right)
        else:
            return True

# @lc code=end
