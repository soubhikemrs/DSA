class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_cnt = 0
        max_cnt = 0
        for num in nums:
            if num == 1:
                curr_cnt += 1
                max_cnt = max(max_cnt, curr_cnt)
            else:
                curr_cnt = 0
        return max_cnt
        