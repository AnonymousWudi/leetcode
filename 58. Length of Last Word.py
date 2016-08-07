# coding=utf-8

"""
    question url: https://leetcode.com/problems/length-of-last-word/
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        length = len(s)
        while length:
            if s[length-1].isalpha():
                return len(s[length-1])
            length -= 1
        return 0