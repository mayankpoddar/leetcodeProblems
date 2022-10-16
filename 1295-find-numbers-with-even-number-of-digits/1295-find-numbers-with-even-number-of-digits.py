class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            digits = 0
            while num != 0:
                digits += 1
                num = num // 10
            if digits % 2 == 0:
                result += 1
        return result