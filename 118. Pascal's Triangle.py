# coding=utf-8

"""
    question url: https://leetcode.com/problems/pascals-triangle/
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if not numRows:
            return result
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        i = 2
        while i < numRows:
            temp_list = [result[i-1][j] + result[i-1][j+1] for j in range(len(result[i-1]) - 1)]
            temp_list.append(1)
            temp_list.insert(0, 1)
            result.append(temp_list)
            i += 1
        return result