class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            mark_idx = abs(nums[i])-1
            if nums[mark_idx] > 0:
                nums[mark_idx] *= -1
        ans = []
        for i,num in enumerate(nums):
            if num > 0:
                ans.append(i+1)
        return ans 