# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        shead=slow.next
        slow.next=None
        curr,prev=shead,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        shead=prev
        node=dummynode=ListNode()
        while shead :
            temp1,temp2=head.next,shead.next
            head.next=shead
            shead.next=temp1
            head,shead=temp1,temp2
            