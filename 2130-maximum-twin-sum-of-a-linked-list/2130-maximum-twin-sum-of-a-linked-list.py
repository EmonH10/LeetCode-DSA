# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:

        nums = [] 

        h = head 

        while(h != None):
            nums.append(h.val) 
            h = h.next 

        maximum = 0
        i = 0
        j = len(nums)-1

        while(i<j):
            maximum = max(maximum,nums[i]+nums[j])
            i+=1
            j-=1

        return maximum

        