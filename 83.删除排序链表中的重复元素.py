# @before-stub-for-debug-begin
from python3problem83 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        pointer = ListNode()
        result = pointer
        while head:
            if head.val not in nums:
                nums.append(head.val)
                pointer.next = ListNode(head.val)
                pointer = pointer.next
            head = head.next
        return result.next

# @lc code=end
