# @before-stub-for-debug-begin
from python3problem110 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root: Optional[TreeNode]) -> int:
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
        # root is null or depth delta <= 1
        if not root or abs(maxDepth(root.left) - maxDepth(root.right)) <= 1:
            return True
        else:
            return False

# @lc code=end
