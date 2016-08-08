# coding=utf-8

"""
    https://leetcode.com/problems/counting-bits/
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = [0]*(num+1)
        a = 1
        for i in range(1, num+1):
            r[i]=r[i-a]+1
            if i == 2*a - 1: a *= 2
        return r