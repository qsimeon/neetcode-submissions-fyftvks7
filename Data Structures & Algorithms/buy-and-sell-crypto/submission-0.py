class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: # no future
            return 0
        max_profit = 0
        for i in range(len(prices)):
            price = prices[i]
            future = prices[i+1:]
            for j in range(len(future)):
                if future[j] < price:
                    continue
                else:
                    profit = future[j] - price
                    if profit > max_profit:
                        max_profit = profit
        return max_profit
