class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low < high:
            s = numbers[low] + numbers[high]
            if s < target:
                low += 1
            elif s > target:
                high -= 1
            else:
                return [low+1, high+1]
        return []