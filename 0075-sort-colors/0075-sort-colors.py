class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countOf0 = 0
        countOf1 = 0
        countOf2 = 0

        n = len(nums)

        for i in range(0,n):

            if nums[i] == 0:
                countOf0 += 1
            elif nums[i] == 1:
                countOf1 += 1
            else:
                countOf2 += 1

        index = 0
        for i in range(0,countOf0):
            nums[index] = 0
            index += 1

        for i in range(0,countOf1):
            nums[index] = 1
            index += 1

        for i in range(0,countOf2):
            nums[index] = 2
            index += 1

        


        