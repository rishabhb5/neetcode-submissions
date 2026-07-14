# O(n^2) Time
# O(1) Space

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
# O(n^2) Time
# O(1) Space

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         s = set()

#         for i in range(len(nums)):
#             if nums[i] in s:
#                 return True
#             s.add(nums[i])
#         return False
# O(n) Time
# O(n) Space

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
# O(nlogn) Time (sort)
# O(1) Space