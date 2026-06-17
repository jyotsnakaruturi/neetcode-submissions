# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        temp = head
        while fast and fast.next :
            slow=slow.next
            fast = fast.next.next
        middle =slow.next
        slow.next = None
        curr = middle
        prev = None 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        head1= head
         
        while head2:
            t1 = head1.next
            t2 = head2.next

            head1.next = head2
            head2.next = t1
            head1 = t1
            head2 = t2
              
 

