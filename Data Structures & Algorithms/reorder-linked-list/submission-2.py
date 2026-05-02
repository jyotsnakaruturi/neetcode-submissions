# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
            if slow == fast :
                break
        shead=slow.next
        slow.next=None
        curr,prev=shead,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        shead = prev
        while shead:
            n1,n2 = head.next,shead.next
            head.next = shead
            shead.next = n1
            head,shead = n1,n2
        