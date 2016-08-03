# coding=utf-8

"""
    question url: https://leetcode.com/problems/roman-to-integer/
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        result = 0
        for i in xrange(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
                result -= 2 * roman_dict[s[i-1]]
            result += roman_dict[s[i]]
        return result