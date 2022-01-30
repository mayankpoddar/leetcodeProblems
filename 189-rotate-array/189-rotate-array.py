class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k != 0:
            toAdd = [nums[i] for i in range(n-k, n)]
            for i in range(n-k-1, -1, -1):
                nums[i+k] = nums[i]
            for i in range(k):
                nums[i] = toAdd[i]
            