class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for i in strs:

            element = "".join(sorted(i))

            if element in d:
                d[element].append(i)
            else:
                d[element] = [i]

        result = []

        for element in d:
            result.append(d[element])

        return result

        

            
                

        