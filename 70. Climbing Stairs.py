# coding=utf-8

"""
    question url: https://leetcode.com/problems/climbing-stairs/
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 2
        result = 0
        cnt = 2
        if n == 1:
            return first
        if n == 2:
            return second
        while cnt < n:
            result = first + second
            first = second
            second = result
            cnt += 1
        return result