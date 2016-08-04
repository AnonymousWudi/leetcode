# coding=utf-8

"""
    question url: https://leetcode.com/problems/house-robber/
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0
        for i in nums:
            first, second = second, max(first+i, second)
        return second