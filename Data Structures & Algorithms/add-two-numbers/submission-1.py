# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        carry =0
        while l1 or l2 or carry:
            total =0
            if l1:
                total= total+l1.val
                l1 = l1.next
            if l2:
                total = total+l2.val
                l2 = l2.next
            if carry :
                total += carry
             
            d = total%10
            carry = total //10
            curr.next = ListNode(d)
            curr = curr.next
        return dummy.next