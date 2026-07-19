class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
    #     for i in range(len(arr) - 1):
    #         large = arr[i + 1]
    #         for j in range(i + 1, len(arr)):
    #             if arr[j] > large:
    #                 large = arr[j]
    #         arr[i] = large
    #     arr[len(arr) - 1] = -1

    #     return arr

    # # O(n^2) time | O(1) space

        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr
    
