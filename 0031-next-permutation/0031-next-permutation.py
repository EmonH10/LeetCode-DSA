class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot = -1
        n = len(nums)

        for i in range(n-2,-1,-1):
            if nums[i+1]>nums[i]:
                pivot = i
                break 


        if pivot == -1:

            i = 0
            j = n-1

            while(i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1

            return nums

        #Just RightMost Bigger

        for i in range(n-1,pivot,-1):
            if nums[i] > nums[pivot]:
                nums[i],nums[pivot] = nums[pivot],nums[i]
                break 

        i = pivot+1
        j = n-1

        while(i<j):
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1

        return nums

        