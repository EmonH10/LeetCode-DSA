class Solution:
    def maxArea(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)-1 

        maxStorage = 0
        storage = 0
        
        while(i<j):

            storage = (j-i)*min(nums[i],nums[j])

            maxStorage = max(maxStorage,storage)

            if nums[i]<nums[j]:
                i+=1

            else:
                j-=1

        return maxStorage




        