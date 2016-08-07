# coding=utf-8

"""
	question url: https://leetcode.com/problems/range-sum-query-immutable/
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        if nums:
            self.value_list = [nums[0]]
            for i in nums[1:]:
                self.value_list.append(i+self.value_list[-1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.value_list[j] - self.value_list[i] + self.nums[i]
        
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)