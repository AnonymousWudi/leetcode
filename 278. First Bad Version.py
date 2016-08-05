# coding=utf-8

"""
    question url: https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        if isBadVersion(1):
            return 1
        while low < high:
            temp = (low + high) / 2
            isBad_one = isBadVersion(temp)
            isBad_two = isBadVersion(temp+1)
            if not isBad_one and isBad_two:
                return temp + 1
            if isBad_one:
                high = temp
            if not isBad_one:
                low = temp
        return low + 1