# coding=utf-8

"""
    question url: https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        temp = 1
        for i in range(len(nums)):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result