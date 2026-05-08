class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        // Solution 1: have a left pointer (ith position) and subtract from
        // every other element to the right of it starting at ith+1 element
        // keep track of the max value found

        var max = 0

        for i in 0..<prices.count {
            for j in (i+1)..<prices.count {
                if prices[j] - prices[i] > max {
                    max = prices[j] - prices[i]
                }
            }
        }

        return max
    }
}
