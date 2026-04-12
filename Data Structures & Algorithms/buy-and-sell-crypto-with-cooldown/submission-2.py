from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def UnBoundedKnapsack(buy_index, index, profit):
            if index >= len(prices):
                return profit
            if prices[buy_index] > prices[index]:
                buy_index = index
            
            prof = profit + (prices[index] - prices[buy_index])
            return max(
                UnBoundedKnapsack(index, index + 2, prof),
                UnBoundedKnapsack(index, index + 1, profit)
            )
        
        return UnBoundedKnapsack(0, 0, 0)

# sol = Solution()
# print(sol.maxProfit([2,1,4]))