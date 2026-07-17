class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        k = 0

        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                nums[k] = nums[i]
                k += 1
                
            
        return k
