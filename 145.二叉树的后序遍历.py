#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive
        # if root:
        #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        # else:
        #     return []
        # iterative
        stack, result = [root], []
        while stack:
            item = stack.pop()
            if isinstance(item, TreeNode):
                stack.extend([item.val, item.right, item.left])
            elif isinstance(item, int):
                result.append(item)
        return result
# @lc code=end

