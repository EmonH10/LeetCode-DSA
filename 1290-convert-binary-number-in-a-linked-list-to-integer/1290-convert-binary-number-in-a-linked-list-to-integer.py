# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:

        nums = []

        while(head != None):
            nums.append(head.val)
            head = head.next 

        result = 0

        for digit in nums:
            result = result*2 + digit

        return result
        