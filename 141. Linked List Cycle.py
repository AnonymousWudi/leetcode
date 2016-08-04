# coding=utf-8

"""
    question url: https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        a = head
        b = head.next
        while b:
            if a.val == b.val:
                return True
            if b.next:
                a = a.next
                b = b.next.next
            else:
                break
        return False