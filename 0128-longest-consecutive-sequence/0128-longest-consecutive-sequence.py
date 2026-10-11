class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        s = set(nums)

        maxCount = 0
    
        for element in s:

            if element-1 not in s:
                count = 1

                while element+1 in s:
                    element += 1
                    count += 1

                maxCount = max(maxCount,count)

        return maxCount
