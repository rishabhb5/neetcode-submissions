class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for l in range(len(nums)):
        #     for r in range(l + 1, min(len(nums), l + k)): # could be near end out of bounds
        #         if nums[l] == nums[r]:
        #             return True

        window = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in window:
                return True
            
            window.add(nums[r])

            if len(window) > k:
                window.remove(nums[l])
                l += 1
        
        return False
        