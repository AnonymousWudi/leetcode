# coding=utf-8

"""
	question url: https://leetcode.com/problems/sum-of-two-integers/
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
if __name__ == '__main__':
	solution = Solution()
	print solution.getSum(2, 2)