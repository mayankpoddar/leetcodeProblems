class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        maximumProfit = -n
        currentProfit = 0
        for i in range(1, n):
            currentProfit += prices[i] - prices[i-1]
            if currentProfit > maximumProfit:
                maximumProfit = currentProfit
            if currentProfit < 0:
                currentProfit = 0
        return max(0,maximumProfit)