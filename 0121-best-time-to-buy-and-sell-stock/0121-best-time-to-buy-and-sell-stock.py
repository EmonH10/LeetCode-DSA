class Solution:
    def maxProfit(self, nums: list[int]) -> int:

        profit = 0
        bestBuy = nums[0]

        for i in range(1,len(nums)):

            if nums[i]<bestBuy:
                bestBuy = nums[i]

            profit = max(profit,nums[i]-bestBuy) 

        return profit
        