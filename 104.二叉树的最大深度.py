# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive
        # if not root:
        #     return 0
        # else:
        #     return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        # iterative
        # level_num: the numbers of node in each level
        level_num = 1 if root else 0
        depth = 0
        queue = [root] if root else []
        while queue:
            item = queue.pop(0)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            level_num -= 1
            # all nodes in each level are scanned, increase depth and update level_num
            if not level_num:
                depth += 1
                level_num = len(queue)
        return depth


# @lc code=end
