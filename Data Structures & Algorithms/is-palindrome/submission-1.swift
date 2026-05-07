class Solution {
    func isPalindrome(_ s: String) -> Bool {
        // Solution 1: Iterate throught the string, left pointer at start of string and right
        // pointer at end of string. Check if they are equal and increment left and
        // decrement right
        // O(n) time | O(n) space

        // format string to remove all spaces
        // manually loop through str chars and append to a new str if not a space
        // use built in function
        //var s1 = s.replacingOccurrences(of: " ", with: "")
        // var s1 = s.filter { $0.isLetter || $0.isNumber }
        // s1 = s1.lowercased()
        // //print(s1)
        
        // let sArr = Array(s1)
        // var l = 0
        // var r = sArr.count - 1

        // for i in 0..<sArr.count {
        //     if sArr[l] != sArr[r] {
        //         return false
        //     }
        //     l += 1
        //     r -= 1
        // }

        // return true

        //---------------------------------------------------------------------------
        
        // Solution 2: format the string and reverse the string and check if they are equal
        var newStr = ""

        // can convert String to Array again or just do the string manip
        for c in s {
            if c.isLetter || c.isNumber {
                newStr.append(c.lowercased())
            }
        }

        if newStr == String(newStr.reversed()) {
            return true
        }
        return false
    }
}
