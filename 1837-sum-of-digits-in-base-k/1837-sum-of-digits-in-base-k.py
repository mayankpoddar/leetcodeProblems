class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n >= k:
            result += n%k
            n = n//k
        result += n
        return result
        