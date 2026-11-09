class Solution:
    def canJump(self, nums: list[int]) -> bool:

        maxReach = 0

        for i in range(0,len(nums)):

            if i > maxReach:
                return False 

            maxReach = max(maxReach,i+nums[i])

        return True


        