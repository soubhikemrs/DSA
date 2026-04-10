class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele_to_idx = {} # this will store index of elements encountered so far
        for i,num in enumerate(nums):
            # the moment we get an element which is target-num
            # we know we have found our answer
            if target-num in ele_to_idx:
                return [i, ele_to_idx[target-num]] # dict helps to get us the index
            ele_to_idx[num] = i  #else simply store the index of the element
        '''even if there are duplicate numbers in nums list, it doesn't matter
        since we have to return only one solution as per the question'''
        return []