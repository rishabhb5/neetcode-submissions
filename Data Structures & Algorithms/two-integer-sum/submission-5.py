class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []


        # Optimized with hashmap - check diff exists in hash
        hm = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in hm:
                hm[nums[i]] = i
            else:
                index = hm.get(val)
                return [index, i]