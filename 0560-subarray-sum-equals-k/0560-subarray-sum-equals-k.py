class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:

        prefixSum = [0]*len(nums)

        prefixSum[0] = nums[0]
        for i in range(1,len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        d = {}
        count = 0

        for i in range(0,len(nums)):

            if prefixSum[i] == target:
                count += 1
            
            value = prefixSum[i] - target

            if value in d:
                count += d[value]

            if prefixSum[i] in d:
                d[prefixSum[i]] += 1

            else:
                d[prefixSum[i]] = 1

        return count
            

        