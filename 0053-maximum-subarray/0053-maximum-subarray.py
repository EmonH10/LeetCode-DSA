class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        currentSum = 0
        maximumSum = nums[0]

        for i in range(0,len(nums)):

            currentSum += nums[i]

            maximumSum = max(maximumSum,currentSum)

            if currentSum < 0:
                currentSum = 0

        return maximumSum
        