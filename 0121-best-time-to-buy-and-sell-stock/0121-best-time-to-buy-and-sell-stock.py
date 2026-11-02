class Solution:
    def maxProfit(self, nums: list[int]) -> int:

        bestBuy = nums[0]
        maxProfit = 0

        for i in range(1,len(nums)):
            if nums[i] < bestBuy:
                bestBuy = nums[i]
            
            maxProfit = max(maxProfit,(nums[i]-bestBuy))

        return maxProfit
        