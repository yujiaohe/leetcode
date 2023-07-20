# @before-stub-for-debug-begin
from python3problem108 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if not length:
            return None
        mid = length // 2
        return TreeNode(val=nums[mid],
                        left=self.sortedArrayToBST(nums[:mid]),
                        right=self.sortedArrayToBST(nums[mid+1:])
                        )
# @lc code=end
