class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create new string, 2 pointers

        i = 0
        j = 0
        res = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if j < len(word2):
                res.append(word2[j])
            i += 1
            j += 1
        return "".join(res)