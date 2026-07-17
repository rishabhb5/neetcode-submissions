class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 # - 1 bc we need it to be in bounds
        
        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = r - 1
            else:
                return m
        
        return -1




# Input: nums = [-1,0,2,4,6,8], target = 6
# -----------------------------------------
# l = 0, r = 5
# m = 2
# nums[m] = 2 < target 6 so l = 3

# l = 3, r = 5
# m = 4
# nums[4] = 6 = target 6 so return 4
