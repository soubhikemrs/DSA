class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in range(1, len(nums)+1):
            xor ^= i
        for num in nums:
            xor ^= num
        
        # now our xor contains the missing and duplicated number
        # we will find the first set bit, then its obvious that at that bit position
        # either our missing number has 0 and duplicated number has 1 at that position
        # or vice-versa
        mask = xor & (~xor + 1)
        num1, num2 = 0, 0
        for i in range(1, len(nums)+1):
            if mask & i:
                num1 ^= i
            else:
                num2 ^= i
        
        for num in nums:
            if mask & num:
                num1 ^= num
            else:
                num2 ^= num

        # we finally get the mimssing and duplicate numbers but we don't know which one is which
        for num in nums:
            if num == num1:
                return [num1, num2]
        return [num2, num1]
