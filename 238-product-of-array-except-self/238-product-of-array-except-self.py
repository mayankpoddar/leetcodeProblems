class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [nums[0]]
        for num in nums[1:]:
            results.append(num*results[-1])
        rightProduct = 1
        for i in range(len(results)-1, 0, -1):
            results[i] = results[i-1] * rightProduct
            rightProduct *= nums[i]
        results[0] = rightProduct
        return results