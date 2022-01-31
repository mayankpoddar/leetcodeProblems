class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for _ in accounts:
            wealth = sum(_)
            if wealth > maxWealth:
                maxWealth = wealth
        return maxWealth