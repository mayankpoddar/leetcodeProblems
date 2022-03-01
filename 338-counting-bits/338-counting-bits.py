class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):
            ones = [ch for ch in bin(i)[2:] if ch == "1"]
            result.append(len(ones))
        return result
        