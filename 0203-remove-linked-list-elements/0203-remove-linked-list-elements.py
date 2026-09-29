# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l = head

        nums = []

        while(l != None):
            value = l.val
            l = l.next

            if value == val:
                continue
            nums.append(value)

        
        dummy = ListNode(0)
        current = dummy

        for i in nums:
            current.next = ListNode(i) 
            current = current.next

        return dummy.next

        

        