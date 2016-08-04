# coding=utf-8

"""
    question url: https://leetcode.com/problems/remove-element/
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.remove(nums[i])
            i -= 1
        return len(nums)