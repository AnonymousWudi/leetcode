# coding=utf-8

"""
    question url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) - 1
        while length > 0:
            if nums[length - 1] == nums[length]:
                nums.pop(length)
            length -= 1
        return len(nums)