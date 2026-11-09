class Solution:
    def eraseOverlapIntervals(self, nums: list[list[int]]) -> int:

        nums.sort(key = lambda x : x[1])

        count = 1
        lastElement = nums[0][1]

        for i in range(1,len(nums)):

            if nums[i][0] >= lastElement:
                count += 1
                lastElement = nums[i][1]

        return len(nums)-count
        