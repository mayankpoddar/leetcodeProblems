class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        leftSum = sum(nums)
        currentSum = 0
        result = []
        for i in range(len(nums)-1, -1, -1):
            result.append(nums[i])
            currentSum += nums[i]
            leftSum -= nums[i]
            if currentSum > leftSum:
                break
        return result
        