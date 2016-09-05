# coding=utf-8

"""
    question url: https://leetcode.com/problems/wiggle-subsequence/
"""

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        muti = nums[1] - nums[0]
        result = 2 if muti != 0 else 1
        for i in range(1, len(nums)-1):
            temp_muti = (nums[i+1] - nums[i]) * muti
            if nums[i+1] - nums[i] == 0:  continue
            if temp_muti <= 0:
                result += 1
            muti = nums[i+1] - nums[i]
        return result

if __name__ == '__main__':
    solution = Solution()
    print solution.wiggleMaxLength([0,0,0])