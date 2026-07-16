class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstWord = strs[0]
        res = ""

        for i in range(len(firstWord)):
            for s in strs:
                if i == len(s) or s[i] != firstWord[i]:
                    return res
            res += firstWord[i]

        return res
