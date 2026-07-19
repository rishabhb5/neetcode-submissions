class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # first thought is 2 separate passes of nums and append to ans[]
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans        