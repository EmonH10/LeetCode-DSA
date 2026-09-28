class Solution:
    def canPlaceFlowers(self, nums: list[int], n: int) -> bool:
        
        l = len(nums)

        #edge cases

        if l == 1 and nums[0] == 0:
            return True

        if l>=2:
            if nums[0] == 0 and nums[1] == 0:
                nums[0] = 1
                n-=1

            if nums[l-1] == 0 and nums[l-2] == 0:
                nums[l-1] = 1
                n-=1

        for i in range(1,len(nums)-1):
            if nums[i] == 0 and nums[i-1] == 0 and nums[i+1]==0:
                n -= 1
                nums[i] = 1

        if n<=0:
            return True
        
        return False
        