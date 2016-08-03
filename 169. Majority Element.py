# coding=utf-8

"""
    question url: https://leetcode.com/problems/majority-element/
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_nums = []
        for i in nums:
            if i in temp_nums:
                continue
            if nums.count(i) >= ((len(nums) + 1) / 2):
                return i
            temp_nums.append(i)