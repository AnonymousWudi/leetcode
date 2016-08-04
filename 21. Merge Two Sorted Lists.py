# coding=utf-8

"""
	question url: https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            while l2:
                if l1.next and l1.val <= l2.val <= l1.next.val:
                    temp = l2
                    l2 = l2.next
                    temp.next = l1.next
                    l1.next = temp
                    l1 = l1.next
                elif l1.next and l1.val < l2.val and l1.next.val < l2.val:
                    l1 = l1.next
                elif not l1.next:
                    l1.next = l2
                    break
        else:
            head = l2
            while l1:
                if l2.next and l2.val <= l1.val <= l2.next.val:
                    temp = l1
                    l1 = l1.next
                    temp.next = l2.next
                    l2.next = temp
                    l2 = l2.next
                elif l2.next and l2.val < l1.val and l2.next.val < l1.val:
                    l2 = l2.next
                elif not l2.next:
                    l2.next = l1
                    break
        return head