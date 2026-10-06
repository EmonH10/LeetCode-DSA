class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()

        digits = "1234567890"

        for element in s:
            if element in digits:
                nums.add(element)
                

        nums = list(nums)
       
        if len(nums)<2:
            return -1

        
        first_max = float("-inf")
        second_max = float("-inf")

        for i in range(0,len(nums)):
            if int(nums[i])>first_max:
                second_max = first_max
                first_max = int(nums[i])

            elif int(nums[i])>second_max:
                second_max = int(nums[i])
                
        return second_max

        