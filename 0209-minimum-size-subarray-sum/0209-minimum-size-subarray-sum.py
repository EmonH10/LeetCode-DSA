class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        currentSum = 0
        minimum = float("inf")
        l = 0

        for r in range(0,len(nums)):

            currentSum += nums[r]
            while(currentSum>=target):
                minimum = min(minimum,r-l+1)
                currentSum = currentSum - nums[l]
                l+=1

        if minimum == float("inf"):
            return 0

        return minimum
        