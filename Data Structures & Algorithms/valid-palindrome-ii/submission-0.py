class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(l, r) -> bool:
            L = l
            R = r

            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
        
        
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return (isPalindrome(L + 1, R) or isPalindrome(L, R - 1))
            L += 1
            R -= 1

        return True

                