class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        
        /* BRUTEFORCE: double for loop check ith element w/ every other element */
        for i in 0..<nums.count {
            for j in i+1..<nums.count {
                if nums[i] == nums[j] {
                    return true
                }
            }
        }
        return false

        /* OPTIMIZED: make a set, iterate through the array and 
        check if the current element in already in the set */

    }
}
