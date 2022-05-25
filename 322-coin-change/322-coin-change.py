class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins, reverse=True)
        n = len(coins)
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
            
        