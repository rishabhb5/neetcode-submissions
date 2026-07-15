class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        fixedLength = len(nums)

        for i in range(fixedLength):
            nums.append(nums[i])

        return nums