class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_dist = 101
        n = len(words)
        for i in range(n):
            if words[i] == target:
                min_dist = min(abs(startIndex-i), n-abs(startIndex-i), min_dist)
        if min_dist == 101:
            return -1
        return min_dist
        
