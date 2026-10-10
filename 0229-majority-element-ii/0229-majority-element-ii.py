class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d = {}

        n = len(nums)

        for element in nums:
            if element in d:
                d[element] += 1
            else:
                d[element] = 1

        print(d)

        result = []

        for element in d:
            if d[element] >n/3:
                result.append(element)

        return result
        