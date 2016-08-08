# coding=utf-8

"""
    question url: https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        if not l1:
            return l2
        if not l2:
            return l1
        head = l1
        while l1.next and l2.next:
            node_val = l1.val + l2.val + flag
            flag = node_val / 10
            node_val %= 10
            l1.val = node_val
            l1 = l1.next
            l2 = l2.next
        if not l1.next:
            l1.next = l2.next
        node_val = l1.val + l2.val + flag
        flag = node_val / 10
        node_val %= 10
        l1.val = node_val
        while l1.next:
            l1 = l1.next
            l1.val += flag
            flag = l1.val / 10
            l1.val %= 10
            if not flag:
                return head
        if flag:
            l1.next = ListNode(1)
        return head