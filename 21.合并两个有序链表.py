# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pointer = result
        while list1 and list2:
            if list1.val <= list2.val:
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                list2 = list2.next
            pointer.next = new_node
            pointer = pointer.next
        # check if is there any elements in list
        while list1:
            new_node = ListNode(list1.val)
            pointer.next = new_node
            pointer = pointer.next
            list1 = list1.next
        while list2:
            new_node = ListNode(list2.val)
            pointer.next = new_node
            pointer = pointer.next
            list2 = list2.next
        return result.next

# @lc code=end
