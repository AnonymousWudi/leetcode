# coding=utf-8

"""
    question url: https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.right, sum-root.val) | self.hasPathSum(root.left, sum-root.val)