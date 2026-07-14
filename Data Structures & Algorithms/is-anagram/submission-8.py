# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         s = sorted(s)
#         t = sorted(t)

#         for i in range(len(s)):
#             if s[i] != t[i]:
#                 return False
        
#         return True
#O(nlogn) Time
#O(n) Space

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         return sorted(s) == sorted(t) # this is better
#O(nlogn) Time
#O(n) Space

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         s_hashmap = {}
#         t_hashmap = {}

#         for i in range(len(s)):
#             s_hashmap[s[i]] = s_hashmap.get(s[i],0) + 1
        
#         for j in range(len(t)):
#             t_hashmap[t[j]] = t_hashmap.get(t[j],0) + 1
        
#         return s_hashmap == t_hashmap























class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        shm = {}
        thm = {}

        for i in range(len(s)):
            shm[s[i]] = shm.get(s[i],0) + 1
            thm[t[i]] = thm.get(t[i],0) + 1
        
        return shm == thm


