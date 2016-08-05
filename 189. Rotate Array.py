# coding=utf-8

"""
    question url: https://leetcode.com/problems/rotate-array/
"""

# 第一种方法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            tail = nums.pop()
            nums.insert(0, tail)
            k -= 1

# 第二种方法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0 or k >= len(nums):
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]