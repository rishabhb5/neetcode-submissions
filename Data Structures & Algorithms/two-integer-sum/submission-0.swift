class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        // Solution: Brute force solution with a double for loop checking
        // ith + jth (i+1) position and checking if it equals the target
        // then returning [i,j]
        // O(n^2) time | O(n) space

        var result = [Int]()

        for i in 0..<nums.count {
            for j in i+1..<nums.count {
                if (nums[i]+nums[j]) == target {
                    result.append(i)
                    result.append(j)
                    
                    return result
                }
            }
        }
        return result

        //-----------------------------------------------------------------

        // Solution: 
    }
}
