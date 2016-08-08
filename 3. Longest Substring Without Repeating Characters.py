# coding=utf-8

"""
    question url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_list = []
        max_len = 0
        for i in s:
            if i in temp_list:
                if len(temp_list) > max_len:
                    max_len = len(temp_list)
                index = temp_list.index(i)
                if index == len(temp_list):
                    temp_list = []
                else:
                    temp_list = temp_list[index+1:]
                temp_list = temp_list + [i]
            else:
                temp_list.append(i)
        return max(len(temp_list), max_len)