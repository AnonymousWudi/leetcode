# coding=utf-8

"""
	question url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getDepth(node):
	if not node:
		return 0
	return max(getDepth(node.left) + 1, getDepth(node.right) + 1)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return getDepth(root)