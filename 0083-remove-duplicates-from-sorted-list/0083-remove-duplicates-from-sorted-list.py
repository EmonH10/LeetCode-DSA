# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        l = head

        d = {}

        while(l != None):
            if l.val not in d:
                d[l.val] = 1
            
            l = l.next

        dummy = ListNode(0)
        current = dummy

        for element in d:
            current.next = ListNode(element)
            current = current.next

        return dummy.next


        