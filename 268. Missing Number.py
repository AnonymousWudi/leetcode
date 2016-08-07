# coding=utf-8

"""
	question url: https://leetcode.com/problems/missing-number/
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        amount = len(nums) * (len(nums) + 1) / 2
        total = 0
        for i in nums:
            total += i
        return amount - total