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
        // O(n) time | O(1) space
        
        // var slow = head
        // var fast = head?.next

        // if slow == nil || fast == nil {
        //     return false
        // }

        // while slow != nil {
        //     if slow?.val == fast?.val {
        //         return true
        //     }
        //     slow = slow?.next
        //     fast = fast?.next?.next
        // }
        
        // return false

        //----------------------------------------------------------------------

        // Solution 2: Using a Set
        // O(n) time | O(n) space using a set (not as optimal as fast/slow pointers)

        var set = Set<ObjectIdentifier>()
        var node = head

        while node != nil {
            let nodeId = ObjectIdentifier(node!)

            if set.contains(nodeId) {
                return true
            }
            else {
                set.insert(nodeId)
                node = node?.next
            }
        }
        return false

        
    }
}
