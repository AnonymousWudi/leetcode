# coding=utf-8

"""
	question url: https://leetcode.com/problems/symmetric-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        def sym_tree(L,R):
            if L and R: 
                return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
            else:
                return L == R
        return sym_tree(root, root)