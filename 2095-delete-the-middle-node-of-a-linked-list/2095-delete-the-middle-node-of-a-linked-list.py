# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        count = 0
        h = head 

        while(h != None):
            h = h.next 
            count += 1

        if count == 1:
            return None

        i = 0
        current = head

        while(i<(count//2)-1):
            current = current.next 
            i+=1

        current.next = current.next.next

        return head
        