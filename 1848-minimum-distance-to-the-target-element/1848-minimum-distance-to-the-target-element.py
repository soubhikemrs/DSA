class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        leftIdx = start
        rightIdx = start
        #Since target always exist, no infinite loop will happen
        while True:
            if leftIdx >= 0:
                if nums[leftIdx] == target:
                    return abs(leftIdx-start)
            elif rightIdx < len(nums):
                if nums[rightIdx] == target:
                    return abs(rightIdx-start)
            leftIdx -= 1
            rightIdx += 1
        return 0