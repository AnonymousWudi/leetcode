# coding=utf-8

"""
    question url: https://leetcode.com/problems/maximum-subarray/
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        largest_num = nums[0]
        temp = 0
        for i in nums:
            if i > largest_num:
                largest_num = i
            temp += i
            if temp < 0:
                temp = 0
            if temp > result:
                result = temp
        if largest_num < 0:
            result = largest_num
        return result