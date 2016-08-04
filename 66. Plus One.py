# coding=utf-8

"""
    question url: https://leetcode.com/problems/plus-one/
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        flag = 1
        while flag and i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
            else:
                flag = 0
        if flag == 1:
            digits.insert(0, 1)
        return digits