class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        n = len(nums)
        prefixSum = [0]*n
        suffixSum = [0]*n

        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1]+nums[i-1]

        for i in range(n-2,-1,-1):
            suffixSum[i] = suffixSum[i+1]+nums[i+1]

        for i in range(0,n):

            if prefixSum[i] == suffixSum[i]:
                return i

        return -1