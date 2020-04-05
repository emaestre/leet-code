class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        prices_len = len(prices)
        for i in range(1, prices_len):
            if(prices[i] > prices[i - 1]):
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit
        