class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}

        for element in nums:
            if element in d:
                return element
            else:
                d[element] = 1

        return -1

              