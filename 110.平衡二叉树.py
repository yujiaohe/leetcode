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
        # 1: from top to buttom
        # def maxDepth(root: Optional[TreeNode]) -> int:
        #     level_num = 1 if root else 0
        #     depth = 0
        #     queue = [root] if root else []
        #     while queue:
        #         item = queue.pop(0)
        #         if item.left:
        #             queue.append(item.left)
        #         if item.right:
        #             queue.append(item.right)
        #         level_num -= 1
        #         if not level_num:
        #             depth += 1
        #             level_num = len(queue)
        #     return depth
        
        # if not root:
        #     return True
        # return abs(maxDepth(root.right)- maxDepth(root.left)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
        # 2: from buttom to top
        self.result = True
        def check(root):
            if not root:
                return 0
            # 计算左右子树高度
            left = check(root.left) + 1
            right = check(root.right) + 1
            if abs(left - right) > 1:
                self.result = False
            return max(left, right)
        check(root)
        return self.result

    

# @lc code=end
