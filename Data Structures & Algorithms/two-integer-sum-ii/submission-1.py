class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hm = {}

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]

        #     if diff not in hm:
        #         hm[numbers[i]] = i
        #     else:
        #         return [hm[diff] + 1, i + 1]
        
        # return []
# O(n) time | O(n) space

#------------------------------------------------

        L = 0
        R = len(numbers) - 1

        while L < R:
            s = numbers[R] + numbers[L]
        
            if s > target:
                R -= 1
            elif s < target:
                L += 1
            else:
                return [L+1, R+1]
        
        return []
    
        