class Solution:
    def eraseOverlapIntervals(self, nums: list[list[int]]) -> int:

        if len(nums) == 0:
            return 0
            
        nums.sort(key = lambda x:x[1])
        lastEndTime = nums[0][1]

        count = 1

        for i in range(1,len(nums)):
            if nums[i][0]>=lastEndTime:
                count+=1
                lastEndTime = nums[i][1]

        return (len(nums)-count)
        
        