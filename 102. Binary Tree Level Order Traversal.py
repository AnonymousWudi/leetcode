# coding=utf-8

"""
    question url: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node_list = [root]
        result = []
        while len(node_list):
            result.append([n.val for n in node_list])
            temp_list = []
            for n in node_list:
                if n.left:
                    temp_list.append(n.left)
                if n.right:
                    temp_list.append(n.right)
            node_list = temp_list
        return result