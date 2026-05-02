# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=head
        N=0
        while start:
            N+=1
            start=start.next
        s=N-n
        if N==n:
            return head.next
        temp=head
        while temp :
            s=s-1
            if s==0:
                temp.next=temp.next.next
                break
            temp=temp.next
        return head
            



        