class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        minimum = len(strs[0])

        for element in strs:
            minimum = min(minimum,len(element))

        i = 0

        while(i<minimum):

            element = strs[0][i]

            for s in strs:

                if s[i] == element:
                    continue 

                else:
                    return strs[0][:i]

            i+=1

        return strs[0][:minimum]