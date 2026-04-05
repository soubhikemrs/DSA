class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height)-1
        curr_area = 0
        max_area = 0
        while low < high:
            curr_area = (high-low)*min(height[low], height[high])
            max_area = max(max_area, curr_area)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area