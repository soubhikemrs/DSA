class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = -1
        high = len(nums)
        curr = 0
        while low < high and curr < high:
            if nums[curr] == 0:
                low += 1
                nums[low], nums[curr] = nums[curr], nums[low]
                curr += 1
            elif nums[curr] == 2:
                high -= 1
                nums[high], nums[curr] = nums[curr], nums[high]
            else:
                curr += 1
           
