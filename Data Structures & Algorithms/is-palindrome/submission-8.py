class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L <= R:
            if s[L].isalnum() == False:
                L += 1
            elif s[R].isalnum() == False:
                R -= 1
            else:
                if s[L].lower() != s[R].lower():
                    return False
                L += 1
                R -= 1
        
        return True