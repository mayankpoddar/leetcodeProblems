class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        num_counts = {}
        for num in arr:
            num_counts[num] = num_counts.get(num, 0) + 1
        num_counts = sorted(list(num_counts.items()), key=lambda x: x[1], reverse=True)
        left = n
        result = 0
        for num, count in num_counts:
            result += 1
            left -= count
            if left <= n//2:
                break
        return result