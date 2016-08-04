# coding=utf-8

"""
    question url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        price_max = 0
        price_min = prices[0]
        i = 0
        while i < len(prices):
            if prices[i] - price_min > price_max:
                price_max = prices[i] - price_min
            if prices[i] < price_min:
                price_min = prices[i]
            i += 1
        return price_max