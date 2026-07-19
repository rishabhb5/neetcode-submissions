class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i not in hm:
                stack.append(i)
            else:
                if len(stack) > 0 and hm[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False