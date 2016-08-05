# coding=utf-8

"""
    question url: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not len(str):
            return 0
        num_list = []
        flag = 0
        flag_two = 0
        for r in str:
            if r == ' ' and not flag_two:
                continue
            if r == '-' and flag == 0:
                flag = 1
                flag_two = 1
                continue
            if r == '+' and flag == 0:
                flag = 2
                flag_two = 1
                continue
            try:
                num_list.insert(0, int(r))
                flag_two = 1
            except ValueError:
                break
        ten = 1
        result = 0
        for n in num_list:
            result += ten * n
            ten *= 10
        if flag == 1:
            result = 0 - result
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result