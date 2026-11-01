class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maximum = 0

        for i in range(0,len(nums)):

            if maximum<i:
                return False

            maximum = max(maximum,i+nums[i])

        return True
        