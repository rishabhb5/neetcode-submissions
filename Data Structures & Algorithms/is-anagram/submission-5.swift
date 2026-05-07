class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        // For all solutions an immediate base case is checking if the length
        // of the strings is the same -> continue if true & return false if not
        
        // Solution1: iterate through each string once
        // When iterating through String s, create a hashmap and keep count of char
        // and count. When iterating through String t check hashmap and decrement 
        // count of each char seen. Then check if the Hashmap is empty*/
        // O(n) time | O (n) space

        // in Swift,  Hashmap is called a Dictionary
        // var hashmap = [Character: Int]()
        // let sArr = Array(s)
        // let tArr = Array(t)

        // for i in 0..<sArr.count {
        //     hashmap[sArr[i], default: 0] += 1 
        // }

        // for j in 0..<tArr.count {
        //     hashmap[tArr[j], default: 0] -= 1

        //     if hashmap[tArr[j]] == 0 {
        //         hashmap.removeValue(forKey: tArr[j])
        //     }
        // }

        // // if there was a mismatch between the strings then there might be some keys
        // // with values of -1. We will be removing all the matches which should be
        // // values of 0s so any -1 values for keys means a mismatch between the strings
        // if hashmap.isEmpty {
        //     return true
        // }
        // else {
        //     return false
        // }
        
        //----------------------------------------------------------------------------

        // Solution 2: Can create 2 Hashmaps instead and add string counts to each and then compare both the Hashmaps at the end -> this instead results
        // in less code but an extra Hashmap. My above solution solves it with just
        // a single Hashmap.

        //----------------------------------------------------------------------------

        // Solution 3: Sort the strings and then compare the Strings
        if s.count != t.count {
            return false
        }

        if s.sorted() == t.sorted() {
            return true
        }

        return false

    }
}
