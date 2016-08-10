# coding=utf-8

"""
    question url: https://leetcode.com/problems/search-for-a-range/
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        index = 0
        if target not in nums:
            return [-1, -1]
        while l <= r:
            index = (l+r)/2
            if nums[index] < target:
                l = index+1
            elif nums[index] > target:
                r = index-1
            else:
                break
        t_from = index
        while nums[t_from] == target:
            t_from -= 1
            if t_from < 0:
                break
        t_from += 1

        t_to = index
        while nums[t_to] == target:
            t_to += 1
            if t_to >= len(nums):
                break
        t_to -= 1
        return [t_from, t_to]


if __name__ == '__main__':
    solution = Solution()
    print solution.searchRange([1, 4], 4)