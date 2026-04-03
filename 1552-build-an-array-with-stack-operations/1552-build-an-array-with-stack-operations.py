class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack_oprs = []
        num, j = 1, 0
        while num <= n and j<len(target):
            stack_oprs.append("Push")
            if num == target[j]:
                j += 1
            else:
                stack_oprs.append("Pop")
            num += 1
        return stack_oprs