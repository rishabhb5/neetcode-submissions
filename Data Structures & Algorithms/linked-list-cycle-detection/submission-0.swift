/**
 * Definition for singly-linked list.
 * class ListNode {
 *     var val: Int
 *     var next: ListNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        // Solution 1: Fast and Slow pointers (Floyd's Tortoise and Hare Problem)
        var slow = head
        var fast = head?.next

        if slow == nil || fast == nil {
            return false
        }

        while slow != nil {
            if slow?.val == fast?.val {
                return true
            }
            slow = slow?.next
            fast = fast?.next?.next
        }
        
        return false

        //----------------------------------------------------------------------

        // Solution 2: Using a Set
        
    }
}
