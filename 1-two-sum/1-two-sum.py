class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutionMap = {}
        for i in range(len(nums)):
            sol = solutionMap.get(nums[i], None)
            if sol is not None:
                return [sol, i]
            else:
                other = target - nums[i]
                solutionMap[other] = i
        return None