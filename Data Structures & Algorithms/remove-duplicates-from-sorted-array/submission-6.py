class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l += 1
            r += 1
        return l + 1 #bc we started l at 0