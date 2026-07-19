class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr) - 1):
            large = arr[i + 1]
            for j in range(i + 1, len(arr)):
                if arr[j] > large:
                    large = arr[j]
            arr[i] = large
        arr[len(arr) - 1] = -1

        return arr
            
