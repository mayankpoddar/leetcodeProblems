class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 0
        result = []
        while i <= n-1 and j <= n-1:
            while nums[i] <= 0:
                i += 1
            positiveNum = nums[i]
            i += 1
            result.append(positiveNum)
            while nums[j] >= 0:
                j += 1
            negativeNum = nums[j]
            j += 1
            result.append(negativeNum)
        return result
        