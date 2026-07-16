class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {} # element : count

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        maxVal = 0
        maxKey = 0
        for k, v in hm.items():
            if v > maxVal:
                maxVal = v
                maxKey = k
        
        return maxKey

