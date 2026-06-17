# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c=0
        while temp :
            c+=1
            temp = temp.next
        find = c-n
        if c == 1:
            return   None
        if find == 0 and c!=1:
            head = head.next
            return head
        temp = head
        c=0
        while temp:
            c+=1
            if c == find:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head

        