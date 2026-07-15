# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
# O(n^2) Time
# O(1) Space

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hm = {} # val : index

#         for i in range(len(nums)):
#             hm[nums[i]] = i
        
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in hm and hm.get(diff) != i:
#                 return [i, hm.get(diff)]
#         return []
# O(n) Time
# O(n) Space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # val : index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            hm[nums[i]] = i

















