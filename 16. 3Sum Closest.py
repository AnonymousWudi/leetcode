# coding=utf-8

"""
    question url: https://leetcode.com/problems/3sum-closest/
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            return
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            aim = target - nums[i]
            x, y = i+1, len(nums)-1
            while x < y:
                if nums[x] + nums[y] < aim:
                    if abs(nums[x] + nums[y] + nums[i] - target) < abs(result-target):
                        result = nums[x] + nums[y] + nums[i]
                    x += 1
                elif nums[x] + nums[y] > aim:
                    if abs(nums[x] + nums[y] + nums[i] - target) < abs(result-target):
                        result = nums[x] + nums[y] + nums[i]
                    y -= 1
                else:
                    return target
        return result