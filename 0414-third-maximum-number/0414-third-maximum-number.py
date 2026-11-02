class Solution:
    def partition(self,nums,low,high):
        pivot = nums[low]
        i = low+1
        j = high

        while(i<=j):

            while(i<=high and nums[i]<= pivot):
                i+=1 
            
            while(j>=low and nums[j]>pivot):
                j-=1

            if i<j:
                nums[i],nums[j] = nums[j],nums[i]

        nums[low],nums[j] = nums[j],nums[low]

        return j

    def quickSort(self,nums,low,high):

        if low<high:
            partitionIndex = self.partition(nums,low,high)

            self.quickSort(nums,low,partitionIndex-1)
            self.quickSort(nums,partitionIndex+1,high)

        return nums

    def thirdMax(self, nums: list[int]) -> int:

        s = set(nums)

        l = list(s)

        if len(l)<3:
            return max(l)

        result = self.quickSort(l,0,len(l)-1)

        return result[-3]
        