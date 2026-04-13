class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_idx = -1 #stores the index of last encountered non-zero element so far
        i = 0 #will use it to traverse the array
        while i < len(nums):
            if nums[i] != 0:
                last_idx += 1
                nums[last_idx], nums[i] = nums[i], nums[last_idx]
            i += 1
        '''automatically as we swap all non-zero elements to the left most side, 
        the right size will be filled with 0s'''
        
