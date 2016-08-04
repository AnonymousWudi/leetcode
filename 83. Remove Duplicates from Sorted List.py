# coding=utf-8

"""
    question url: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_head = head
        while temp_head:
            if temp_head.next and temp_head.val == temp_head.next.val:
                temp_head.next = temp_head.next.next
                continue
            temp_head = temp_head.next
        return head