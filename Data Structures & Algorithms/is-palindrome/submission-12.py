class Solution:
    def isPalindrome(self, s: str) -> bool:
        # L = 0
        # R = len(s) - 1

        # while L < R and len(s) > 0:
        #     while s[L].isalnum() == False and L < R:
        #         L += 1
            
        #     while s[R].isalnum() == False and R > L:
        #         R -= 1
            
        #     if s[L].lower() != s[R].lower():
        #         return False
        #     L += 1
        #     R -= 1
        
        # return True

#----------------------------------------------------------

        L = 0
        R = len(s) - 1

        while L < R:
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
