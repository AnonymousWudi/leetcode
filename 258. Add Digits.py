# coding=utf-8

"""
	question url: https://leetcode.com/problems/add-digits/
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num != 0:
        	result += num % 10
        	if result > 9:
        		result = result / 10 + result % 10
        	num /= 10
        return result

if __name__ == '__main__':
	solution = Solution()
	print solution.addDigits(19)