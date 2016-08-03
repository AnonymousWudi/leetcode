# coding=utf-8

"""
	question url: https://leetcode.com/problems/move-zeroes/
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        while count < len(nums):
            if nums[index] == 0:
                nums.remove(0)
                nums.append(0)
                index -= 1
            index += 1
            count += 1
        return nums

if __name__ == '__main__':
	solution = Solution()
	print solution.moveZeroes([1, 0, 1])