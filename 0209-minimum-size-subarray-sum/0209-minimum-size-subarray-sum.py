class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        l = 0
        minimum = float("inf")
        currentSum = 0

        for r in range(0,len(nums)):
            currentSum += nums[r]

            while currentSum>=target:
                minimum = min(minimum,r-l+1)
                currentSum -= nums[l]
                l+=1

        if minimum == float("inf"):
            return 0

        return minimum
            
            
        