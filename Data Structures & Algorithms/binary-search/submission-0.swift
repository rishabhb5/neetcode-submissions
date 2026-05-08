class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        // Solution 1: get the mid point of the list -> check if it is greater
        // or less than the target number we are looking for, move the bounds
        // accordingly with 2 pointers left and right

        var l = 0
        var r = nums.count - 1

        while (l <= r) {
            let mid = (l + r) / 2

            if nums[mid] < target {
                l = mid + 1
            }
            else if nums[mid] > target {
                r = mid - 1
            }
            else {
                return mid
            }
        }

        return -1

    }
}
