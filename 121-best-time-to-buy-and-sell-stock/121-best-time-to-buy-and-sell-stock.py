class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        profits = [0]*n
        profits[0] = prices[0]
        for i in range(1, n):
            profits[i] = prices[i] - prices[i-1]
        del prices
        maximumProfit = -1000
        currentProfit = 0
        for i in range(1, n):
            currentProfit += profits[i]
            if currentProfit > maximumProfit:
                maximumProfit = currentProfit
            if currentProfit < 0:
                currentProfit = 0
        return max(0,maximumProfit)