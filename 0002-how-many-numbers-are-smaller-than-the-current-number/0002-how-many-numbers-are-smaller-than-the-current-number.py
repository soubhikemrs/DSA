class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    cnt += 1
            ans.append(cnt)
        return ans