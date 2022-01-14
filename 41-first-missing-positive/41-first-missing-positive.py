class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set([num for num in nums if num > 0]))
        n = len(nums)
        if n == 0:
            return 1
        min_num = nums[0]
        max_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
        if min_num != 1:
            return 1
        if n == max_num:
            return max_num+1
        elif n == max_num - 1:
            return ((n+1)*(n+2))//2 - sum(nums)
        else:
            nums.sort()
            for i in range(1, n):
                if nums[i] - nums[i-1] != 1:
                    return nums[i-1] + 1