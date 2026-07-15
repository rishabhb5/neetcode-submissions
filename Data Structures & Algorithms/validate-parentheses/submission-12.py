class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")":"(", "}":"{", "]":"[",}
        stack = []

        for i in range(len(s)):
            if s[i] not in hm:
                stack.append(s[i])
            else:
                # going through s still so stack should still have elements
                # in it
                if len(stack) == 0 or stack.pop() != hm[s[i]]:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
# O(n) Time
# O(n) Space
