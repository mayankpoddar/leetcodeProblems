class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        results = 0
        i = 0
        while i <= n-3:
            d = nums[i+1] - nums[i]
            if nums[i+2] - nums[i+1] != d:
                i += 1
                continue
            j = i + 3
            while j < n and nums[j] - nums[j-1] == d:
                j += 1
            currentAPLength = j-i
            i = j-1
            results += ((currentAPLength-2)*(currentAPLength-1))//2
        return results