# @before-stub-for-debug-begin
from python3problem144 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive
        # if root:
        #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # else:
        #     return []
        # iterative
        stack, result = [root], []
        while stack:
            item = stack.pop()
            if isinstance(item, TreeNode):
                stack.extend([item.right, item.left, item.val])
            elif isinstance(item, int):
                result.append(item)
        return result
            


# @lc code=end

