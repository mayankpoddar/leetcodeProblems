class Solution:
    def sumZero(self, n: int) -> List[int]:
        results = []
        if n % 2:
            results.append(0)
        for i in range(1, 1 + n//2):
            results.append(i)
            results.append(-i)
        return results
            