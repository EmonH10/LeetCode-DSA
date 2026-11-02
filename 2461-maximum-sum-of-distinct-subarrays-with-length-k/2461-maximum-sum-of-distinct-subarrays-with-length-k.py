class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:

        freq = {}

        currentSum = 0
        maximumSum = 0

        for i in range(0,k):
            currentSum += nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        if len(freq) == k:
            maximumSum = currentSum

        for i in range(k,len(nums)):
            currentSum = currentSum + nums[i] - nums[i-k]
            freq[nums[i-k]] -= 1

            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]

            if nums[i] in freq:
                freq[nums[i]] += 1

            else:
                freq[nums[i]] = 1

            if len(freq) == k:
                maximumSum = max(maximumSum,currentSum)


        return maximumSum
        