class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums_dict:Dict[int, List[int]] = {}
        n = len(nums)
        min_dist_list = [n]*n
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = []
            nums_dict[num].append(i) #value is list of indices already sorted since traversing incrementally
            if len(nums_dict[num]) >= 2:
                min_dist_list[i] = min(i-nums_dict[num][-2], min_dist_list[i])
                min_dist_list[nums_dict[num][-2]] = min(min_dist_list[i],min_dist_list[nums_dict[num][-2]])

        min_dist_list[0] = min(min_dist_list[0], n-(nums_dict[nums[0]][-1] - 0)) 

        ans = []
        for query in queries:
            key = nums[query]
            if len(nums_dict[key]) == 1:
                ans.append(-1)
            else:
                min_dist = n
                if nums_dict[key][0] == query:
                    min_dist = min(min_dist_list[query], n-(nums_dict[key][-1] - query))
                else:
                    min_dist = min(min_dist_list[query], n-(query-nums_dict[key][0]))
                ans.append(min_dist)
        return ans
