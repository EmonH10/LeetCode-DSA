class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        countOf0 = 0
        countOf1 = 0


        for i in range(0,len(nums)):
            if nums[i] == 0:
                countOf0 += 1

        for i in range(0,len(nums)):
            if nums[i] == 1:
                countOf1 += 1

        print(countOf0)
        print(countOf1)

        k = 0
        i = 0

        while(i < countOf0):
            nums[i] = 0
            i+=1
            k+=1

        j = 0
        while(j<countOf1):
            nums[k] = 1
            k+=1
            j+=1

        while(k<len(nums)):
            nums[k] = 2
            k+=1

        