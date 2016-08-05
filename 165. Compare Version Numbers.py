# coding=utf-8

"""
    question url: https://leetcode.com/problems/compare-version-numbers/
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        i = len(version1) - 1
        while i >= 0 and not int(version1[i]):
            version1.pop()
            i -= 1
        i = len(version2) - 1
        while i >= 0 and not int(version2[i]):
            version2.pop()
            i -= 1
        for i in range(max(len(version1), len(version2))):
            if i >= len(version1):
                return -1
            elif i >= len(version2):
                return 1
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        return 0