class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        left = 0
        right = n - 1
        while left != right:
            if height[right] > height[left]:
                current_area = height[left]*(right-left)
                left += 1
            else:
                current_area = height[right]*(right-left)
                right -= 1
            max_area = max(max_area, current_area)
        return max_area