# coding=utf-8

"""
    question url: https://leetcode.com/problems/reverse-integer/
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        x = int(str(x)[::-1])
        if flag:
            x = -x
        if -2147483648 < x < 2147483647:
            return x
        return 0