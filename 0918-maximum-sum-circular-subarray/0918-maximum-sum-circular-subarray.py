"""
A circular subarray max sum is either:
1. The **normal max subarray** (Kadane’s) — i.e., subarray doesn't wrap.   
2. The **wraparound case** = `totalSum - minSubarraySum`

Won’t the `minSum` subarray **overlap** with `maxSum`, causing wrong answer?  
What if they both point to the same subarray?
Actually — it **doesn’t matter** even if `minSum` and `maxSum` point to **same or overlapping subarrays**, because:
- We **never combine both subarrays** in our final answer.    
- We’re just comparing two sums:    
    1. `maxSum` — standard (non-wrap) subarray sum        
    2. `total - minSum` — circular subarray sum       

==They are **independent computations** — and we pick the one that gives the higher result.==
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_mx_sum = cur_mn_sum = res_mx = res_mn = nums[0]
        total_sum = sum(nums)
        for i in range(1, len(nums)):
            cur_mx_sum = max(cur_mx_sum+nums[i], nums[i])
            cur_mn_sum = min(cur_mn_sum+nums[i], nums[i])

            res_mx = max(res_mx, cur_mx_sum)
            res_mn = min(res_mn, cur_mn_sum)
        
        if res_mx < 0:
            return res_mx
        return max(res_mx, total_sum-res_mn) 