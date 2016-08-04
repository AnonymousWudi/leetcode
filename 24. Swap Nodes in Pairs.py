# coding=utf-8

"""
    question url: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp_head = head
        a = temp_head.next
        b = a.next
        temp_head.next = b
        a.next = temp_head
        head = a
        while temp_head.next:
            if not temp_head.next.next:
                break
            a = temp_head.next
            b = a.next.next
            temp_head.next = a.next
            a.next.next = a
            a.next = b
            temp_head = a
        return head