# coding=utf-8

"""
    question url: https://leetcode.com/problems/pascals-triangle-ii/
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 0
        result = [1]
        while i < rowIndex:
            result.append(0)
            j = i + 1
            while j > 0:
                result[j] += result[j-1]
                j -= 1
            i += 1
        return result