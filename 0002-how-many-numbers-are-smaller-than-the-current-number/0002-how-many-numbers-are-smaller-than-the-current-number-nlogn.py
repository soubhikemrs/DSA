class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        sorted_nums = sorted(nums, reverse=True)
        d = {}
        for i,num in enumerate(sorted_nums):
            d[num] = n-i-1
        
        for num in nums:
            ans.append(d[num])
        return ans
