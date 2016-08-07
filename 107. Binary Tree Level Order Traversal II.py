# coding=utf-8

"""
	question url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tree_list = [root]
        temp_list = []
        result_list = []
        while len(tree_list):
            result_list.insert(0, [r.val for r in tree_list])
            length = len(tree_list)
            temp_list = []
            for r in tree_list:
                if r.left:
                    temp_list.append(r.left)
                if r.right:
                    temp_list.append(r.right)
            tree_list = temp_list
        return result_list