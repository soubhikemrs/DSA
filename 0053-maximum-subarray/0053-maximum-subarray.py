# At every step, we decide whether to continue the previous subarray
# or start afresh.
# This greedy decision helps us to get the best local subarray
# The max_sum stores the best sum out of the best local subarrays that we have gotten
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        # this works even if all elements are -ve
        return max_sum
