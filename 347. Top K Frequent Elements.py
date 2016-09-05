# coding=utf-8

"""
    question url: https://leetcode.com/problems/top-k-frequent-elements/
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numDict = {}
        for n in nums:
            if n in numDict.keys():
                numDict[n] += 1
            else:
                numDict[n] = 1
        return [num[0] for num in sorted(numDict.items(), key=lambda x: x[1], reverse=True)][:k]

if __name__ == '__main__':
    solution = Solution()
    print solution.topKFrequent([1,1,1,2,2,3], 2)