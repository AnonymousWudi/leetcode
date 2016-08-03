# coding=utf-8

"""
    question url: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if not nums2:
                break
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result