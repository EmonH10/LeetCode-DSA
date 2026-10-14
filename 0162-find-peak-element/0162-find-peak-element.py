class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        n = len(nums)
        high = n-1

        if n == 1:
            return 0

        while(low<=high):
            mid = (low+high)//2

            if mid == 0 and nums[mid]>nums[mid+1]:
                return 0

            if mid == n-1 and nums[mid]>nums[mid-1]:
                return n-1

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid-1

        return -1

        