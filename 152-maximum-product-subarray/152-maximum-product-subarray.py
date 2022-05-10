class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currentProd = 1
        maxProd = -2**32 - 1
        for i in range(n):
            currentProd *= nums[i]
            if currentProd > maxProd:
                maxProd = currentProd
            if currentProd == 0:
                currentProd = 1
        currentProd = 1
        for i in range(n-1, -1, -1):
            currentProd *= nums[i]
            if currentProd > maxProd:
                maxProd = currentProd
            if currentProd == 0:
                currentProd = 1
        return maxProd