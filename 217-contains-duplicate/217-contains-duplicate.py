class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        current_set = set([nums[0]])
        for num in nums[1:]:
            if num in current_set:
                return True
            current_set.add(num)
        return False
            
        