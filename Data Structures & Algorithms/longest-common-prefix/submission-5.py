class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        firstWord = strs[0]

        for i in range(len(firstWord)):
            for s in strs:
                if i == len(s) or firstWord[i] != s[i]:
                    return res
            res += firstWord[i]
        
        return res
                
