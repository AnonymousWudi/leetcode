# coding=utf-8

"""
    question url: https://leetcode.com/problems/excel-sheet-column-title/
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letter_list = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        result = ''
        if not n:
            return result
        while n:
            if n % 26 == 0:
                result = letter_list[n % 26] + result
                n = n / 26 - 1
            else:
                result = letter_list[n % 26] + result
                n /= 26

        return result