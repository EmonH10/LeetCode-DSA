class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxIndex = 0

        for i in range(0,len(nums)):
            if maxIndex<i:
                return False
            maxIndex = max(maxIndex,i+nums[i])

        return True