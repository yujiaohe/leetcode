#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_dict = {}
        while head:
            if head in node_dict:
                return True
            else:
                node_dict[head] = 1
            head = head.next
        return False
        
# @lc code=end

