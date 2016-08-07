# coding=utf-8

"""
	question url: https://leetcode.com/problems/add-binary/
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        binary = 0
        if len(b) > len(a):
            a, b = b, a
        len_a = len(a)
        len_b = len(b)
        flag = 0
        while len_b:
            binary = int(a[len_a-1]) + int(b[len_b-1])
            if flag:
                binary += 1
            result = str(binary % 2) + result
            flag = binary / 2
            len_a -= 1
            len_b -= 1
        if len_a:
            while flag and len_a:
                binary = int(a[len_a-1]) + 1
                result = str(binary % 2) + result
                flag = binary / 2
                len_a -= 1
            result = a[:len_a] + result
        if flag:
            result = '1' + result
        return result