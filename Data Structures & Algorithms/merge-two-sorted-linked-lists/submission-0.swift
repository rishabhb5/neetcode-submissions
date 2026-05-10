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
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        // Solution: given 2 sorted linked lists, create a dummy node with
        // value 0
        // O(n) time | O(n) space

         // dummy node that is guaranteed to exist unlike list1 and list2
         // that come from function inputs so those are optional
        var dummy = ListNode(0)
        var newList = dummy // this pointer will build list on top of

        // need these to refer to the LinkedLists bc cant manipulate them
        // directly bc list1 and list2 are instantiated with let
        var l1 = list1
        var l2 = list2

        while (l1 != nil && l2 != nil) {
            if l1!.val < l2!.val {  // need to be unwrapped bc of input lists
                
                // doesn't need to be unwrapped bc newList is refering to dummy
                // which guarantees to exist
                newList.next = l1

                l1 = l1?.next
            }
            else  {
                newList.next = l2
                l2 = l2?.next
            }
            newList = newList.next!
        }

        if l1 != nil {
            newList.next = l1
        }
        else {
            newList.next = l2
        }

        // dummy is still a node that is before newList
        // newList was built on top of dummy so by returning dummy.next
        // we can return the actual new list
        return dummy.next 
    }
}
