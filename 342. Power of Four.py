# coding=utf-8

"""
    question url: https://leetcode.com/problems/power-of-four/
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        while num:
            if num % 4 != 0 and num != 1:
                return False
            num /= 4
        return True