class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def UnBoundedKnapsack(buy_index,index,profit):
            if index >= len(prices):
                return profit
            if prices[buy_index]>prices[index]:
                buy_index = index
            prof = profit + (prices[index] - prices[buy_index])
            return max(UnBoundedKnapsack(index,index+2,prof),
            UnBoundedKnapsack(index,index+1,profit))
        return UnBoundedKnapsack(0,0,0)
