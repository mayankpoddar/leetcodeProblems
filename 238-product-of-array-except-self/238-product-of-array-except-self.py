class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = nums[:]
        for i in range(1, n):
            results[i] *= results[i-1]
        rightProduct = 1
        for i in range(len(results)-1, 0, -1):
            results[i] = results[i-1] * rightProduct
            rightProduct *= nums[i]
        results[0] = rightProduct
        return results