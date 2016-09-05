# coding=utf-8

"""
    question url: https://leetcode.com/problems/find-the-difference/
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_list = list(t)
        for letter in s:
            t_list.remove(letter)
        return ''.join(t_list)
