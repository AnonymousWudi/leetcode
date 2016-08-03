# coding=utf-8

"""
	question url: https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
        	return True
        if p and q and p.val == q.val:
        	return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        return False