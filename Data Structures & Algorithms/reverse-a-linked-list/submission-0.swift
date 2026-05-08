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
    func reverseList(_ head: ListNode?) -> ListNode? {
        // Solution 1: Iterative. Need a prev node, curr node that initially
        // equal to head bc we can't manipulate head direclty bc it is
        // instantiated with a let. Also need a n node that points to curr.next
        // so it holds the rest of the list. Iterate in a while loop while curr
        // is != nil holding the rest of the list and moving the prev and curr
        // pointers up setting curr?.next to the prev

        var prev: ListNode? = nil
        var curr = head // can't use head directly bc it's set as a let

        while curr != nil {
            let n = curr?.next // this now holds rest of list
            curr?.next = prev
            prev = curr
            curr = n
        }
        
        return prev

        //---------------------------------------------------------------------


    }
}
