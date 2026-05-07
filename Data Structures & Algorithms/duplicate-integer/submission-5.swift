class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        
        /* BRUTEFORCE: double for loop check ith element w/ every other element */
        // O(n^2) time | O(1) space/memory 
        // for i in 0..<nums.count {
        //     for j in i+1..<nums.count {
        //         if nums[i] == nums[j] {
        //             return true
        //         }
        //     }
        // }
        // return false

        /* OPTIMIZED: make a set, iterate through the array and 
        check if the current element in already in the set */
        // O(n) time | O(n) space bc could be up to n elements in the Set
        var set = Set<Int>()
        
        for i in 0..<nums.count {
            if set.contains(nums[i]) {
                return true
            }
            else {
                set.insert(nums[i])
            }
        }
        return false
    }
}
