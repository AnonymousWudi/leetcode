# coding=utf-8

"""
	question url: https://leetcode.com/problems/valid-parentheses/
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_stack = []
        for i in s:
            if i in ('(', '{', '['):
                char_stack.append(i)
                continue
            if i in (')', '}', ']') and not char_stack:
                return False
            if i == ')' and char_stack.pop() != '(':
                return False
            elif i == '}' and char_stack.pop() != '{':
                return False
            elif i == ']' and char_stack.pop() != '[':
                return False
        return char_stack == []