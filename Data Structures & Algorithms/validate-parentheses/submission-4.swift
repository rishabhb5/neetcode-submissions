class Solution {
    func isValid(_ s: String) -> Bool {
        // Solution: Create a hashmap for mappings of the closing to opening
        // parentheses. Create a stack for all of the opening parentheses.

        var hashmap = [Character: Character]()
        var stack = [Character]()

        hashmap[")"] = "("
        hashmap["}"] = "{"
        hashmap["]"] = "["

        for c in s {
            
            if hashmap[c] == nil {
                stack.append(c)
            }
            else {

                // if hashmap[c] == stack.last! {
                //     stack.removeLast()
                // }
                // else {
                //     return false
                // }
                 if stack.isEmpty {
                    return false
                }
                if hashmap[c] != stack.last {
                    return false
                }
                stack.removeLast()
            }
        }

        if stack.isEmpty {
            return true
        }
        
        return false
    }
}
