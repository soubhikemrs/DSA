class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A different way to solve using python sort function
        nums.sort(key=lambda x : x==0)

