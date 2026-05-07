class Solution {
    func isPalindrome(_ s: String) -> Bool {
        // Iterate throught the string, left pointer at start of string and right
        // pointer at end of string. Check if they are equal and increment left and
        // decrement right

        // format string to remove all spaces
        // manually loop through str chars and append to a new str if not a space
        // use built in function
        //var s1 = s.replacingOccurrences(of: " ", with: "")
        var s1 = s.filter { $0.isLetter || $0.isNumber }
        s1 = s1.lowercased()
        //print(s1)
        
        let sArr = Array(s1)
        var l = 0
        var r = sArr.count - 1

        for i in 0..<sArr.count {
            if sArr[l] != sArr[r] {
                return false
            }
            l += 1
            r -= 1
        }

        return true

    }
}
