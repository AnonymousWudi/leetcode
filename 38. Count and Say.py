# coding=utf-8

"""
    question url: https://leetcode.com/problems/count-and-say/
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ['1']
        n -= 1
        while n:
            temp_list = []
            start = 0
            letter = result[0]
            for i in range(1, len(result)):
                if result[i] == letter:
                    continue
                else:
                    temp_list = temp_list + [str(i-start)] + [letter]
                    start = i
                    letter = result[i]
            temp_list = temp_list + [str(len(result)-start)] + [letter]
            result = temp_list
            n -= 1
        return ''.join(result)