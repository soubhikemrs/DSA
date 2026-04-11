"""
unlike maximum subarray sum, where at every step we had to decide
whether to extend the current subarray or to start afresh,
here we have three choices to make since even if pdt < 0, it can become
positive in future.
So we will take care of both current max and current min products
and finally get the best max overall product.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_maxp = curr_minp = res = nums[0]
        for i in range(1, len(nums)):
            temp_max = curr_maxp 
            curr_maxp = max(curr_maxp*nums[i], nums[i], curr_minp*nums[i])
            # curr_maxp already updated, but noting to worry as we have its old value in temp_max
            curr_minp = min(curr_minp*nums[i], nums[i], temp_max*nums[i])

            res = max(res, curr_maxp)
        return res