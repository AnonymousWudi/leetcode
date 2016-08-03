# coding=utf-8

"""
    question url: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        a = head.next
        b = a.next
        head.next = None
        while b:
            a.next = head
            head = a
            a = b
            b = b.next
        a.next = head
        return a