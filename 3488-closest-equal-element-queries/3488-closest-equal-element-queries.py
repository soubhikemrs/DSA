from collections import defaultdict
from typing import List
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Group the indices
        # key = element value
        # value = list of indices of that element in nums
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        # precompute min distance for each index
        min_dist = [-1]*n
        for ele, indices in pos.items():
            k = len(indices)
            if k == 1:
                continue
            for j in range(k):
                curr = indices[j]
                next = indices[(j+1)%k]
                prev = indices[(j-1+k)%k]
                d1 = abs(curr-next)
                d2 = abs(curr-prev)
                d3 = n - d1
                d4 = n - d2
                min_dist[curr] = min(d1, d2, d3, d4)
        ans = []
        for query in queries:
            ans.append(min_dist[query])
        return ans