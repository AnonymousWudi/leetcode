# coding=utf-8

"""
	question url: https://leetcode.com/problems/happy-number/
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp_list = []
        temp_n = 0
        while n != 1:
            for i in str(n):
                temp_n += int(i) * int(i)
            n = temp_n
            temp_n = 0
            if n in temp_list:
                return False
            temp_list.append(n)
        return True