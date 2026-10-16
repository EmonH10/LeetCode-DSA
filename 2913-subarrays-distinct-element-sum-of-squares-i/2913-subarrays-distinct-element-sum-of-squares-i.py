class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        total = 0

        for i in range(0,len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j])

                total += len(s)*len(s)

        return total


        