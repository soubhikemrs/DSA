class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_sum_mx = nums[0]
        cur_sum_mn = min_sum = nums[0]
        max_sum = 0
        for i in range(1, len(nums)):
            cur_sum_mx = max(cur_sum_mx+nums[i], nums[i])
            cur_sum_mn = min(cur_sum_mn+nums[i], nums[i])

            max_sum = max(cur_sum_mx, max_sum)
            min_sum = min(cur_sum_mn, min_sum)
        
        return max(abs(max_sum), abs(min_sum))