# coding=utf-8

"""
	question url: https://leetcode.com/problems/valid-palindrome/
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l, r = 0, len(s) - 1
       	while l < r:
       		if not ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'):
       			l += 1
       			continue
       		if not ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'):
       			r -= 1
       			continue
       		if not s[l] == s[r]:
       			return False
       		else:
       			l += 1
       			r -= 1
       	return True