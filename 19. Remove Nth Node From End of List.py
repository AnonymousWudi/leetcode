# coding=utf-8

"""
	question url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a = head
        b = head
        while n:
            b = b.next
            n -= 1
        if not b:
            return head.next
        while b.next:
            a = a.next
            b = b.next
        a.next = a.next.next
        return head