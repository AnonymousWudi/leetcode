# coding=utf-8

"""
    question url: https://leetcode.com/problems/3sum/
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            amount = -nums[i]
            x, y = i+1, len(nums)-1
            while x < y:
                if nums[x] + nums[y] < amount:
                    x += 1
                elif nums[x] + nums[y] > amount:
                    y -= 1
                else:
                    result.add((nums[i], nums[x], nums[y]))
                    x += 1
                    y -= 1
        return list(result)