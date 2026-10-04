class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        bestBuy = nums[0]

        for i in range(1,len(nums)):
            if nums[i]>bestBuy:
                profit = max(profit,nums[i]-bestBuy)
            else:
                bestBuy = nums[i]

        return profit
        