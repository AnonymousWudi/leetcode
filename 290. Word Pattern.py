# coding=utf-8

"""
	question url: https://leetcode.com/problems/word-pattern/
"""

class Solution(object):
	def wordPattern(self, pattern, str):
		"""
        :type pattern: str
        :type str: str
		:rtype: bool
		"""
		pattern_list = []
		str = str.split(' ')
		if not len(pattern) == len(str):
			return False
		for i in range(len(pattern)): 
			flag = 0
			for key, value in pattern_list:
				if key == pattern[i] and value == str[i]:
					flag = 1
					break
				if (key == pattern[i] and value != str[i]) or (key != pattern[i] and value == str[i]):
					return False
			if not flag:
				pattern_list.append((pattern[i], str[i]))
		return True