# coding=utf-8

"""
    question url: https://leetcode.com/problems/guess-number-higher-or-lower/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        m = 1
        while low < high:
            m = (low + high) / 2
            g = guess(m)
            if g == 0:
                return m
            elif g > 0:
                low = m + 1
            elif g < 0:
                high = m - 1
        return low