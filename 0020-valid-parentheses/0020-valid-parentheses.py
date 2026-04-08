class Solution:
    def is_matching(self, op, cl):
        return ((op == "(" and cl == ")") or
            (op == "{" and cl == "}") or
            (op == "[" and cl == ']'))

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack and self.is_matching(stack[-1], ch):
                    stack.pop()
                else:
                    return False
        return stack == []