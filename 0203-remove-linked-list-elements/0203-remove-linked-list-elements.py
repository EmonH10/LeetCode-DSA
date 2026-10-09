# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        
        nums = []

        h = head

        while(h != None):
            nums.append(h.val)
            h = h.next

        arr = []

        for i in nums:
            if i == val:
                continue
            arr.append(i)

        dummy = ListNode(0)
        current = dummy

        for i in arr:
            current.next = ListNode(i)
            current = current.next

        return dummy.next