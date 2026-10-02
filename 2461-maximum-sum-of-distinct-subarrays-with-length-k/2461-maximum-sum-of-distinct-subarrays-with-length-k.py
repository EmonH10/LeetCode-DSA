class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        maximumSum = 0
        currentSum = 0

        freq = {}

        for i in range(0,k):
            currentSum += nums[i]
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        if len(freq) == k:
            maximumSum = currentSum

        
        for l in range(k,len(nums)):

            j = l
            i = j-k

            currentSum = currentSum - nums[i] + nums[j]

            freq[nums[i]] -= 1

            if freq[nums[i]] == 0:
                del freq[nums[i]]

            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1

            if len(freq) == k:
                maximumSum = max(maximumSum,currentSum)


        return maximumSum







  


            

        