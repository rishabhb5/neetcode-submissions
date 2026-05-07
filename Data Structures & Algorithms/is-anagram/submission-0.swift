class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        /* BruteForce: iterate through each string once
        When iterating through String s, create a hashmap and keep count of char and
        count. When iterating through String t check hashmap and decrement count of
        each char seen. Then check if the Hashmap is empty*/

        // in Swift,  Hashmap is called a Dictionary
        var hashmap = [Character: Int]()
        let sArr = Array(s)
        let tArr = Array(t)

        for i in 0..<sArr.count {
            hashmap[sArr[i], default: 0] += 1 
        }

        for j in 0..<tArr.count {
            hashmap[tArr[j], default: 0] -= 1

            if hashmap[tArr[j]] == 0 {
                hashmap.removeValue(forKey: tArr[j])
            }
        }

        if hashmap.isEmpty {
            return true
        }
        else {
            return false
        }

        


    }
}
