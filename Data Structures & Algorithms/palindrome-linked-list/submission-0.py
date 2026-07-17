# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        mid = ListNode(slow.val)
        
        prev = None
        while slow != None: # want slow to overflow so prev is last
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        l = head
        r = prev
        while r != None:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True