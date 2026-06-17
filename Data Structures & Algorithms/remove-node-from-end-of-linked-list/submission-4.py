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
        if find == 0:
            head.val = 0
            return   None
        temp = head
        c=0
        while temp:
            c+=1
            if c == find:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head

        