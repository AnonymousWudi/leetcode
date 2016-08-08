# coding=utf-8

"""
    question url: https://leetcode.com/problems/combination-sum/
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.recursionSum(candidates, target, 0, [], result)
        return result

    def recursionSum(self, candidates, target, index, temp_list, ans):
        if target < 0: return
        elif target == 0:
            ans.append(temp_list)
            return
        for i in range(index, len(candidates)):
            self.recursionSum(candidates, target - candidates[i], i, temp_list+[candidates[i]], ans)