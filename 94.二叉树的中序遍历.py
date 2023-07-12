#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recusion
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        # iteration
        stack, result = [root], []
        while stack:
            item = stack.pop()
            if isinstance(item, TreeNode):
                stack.extend([item.right, item.val, item.left])
            elif isinstance(item, int):
                result.append(item)
        return result

# @lc code=end
