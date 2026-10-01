class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minimum = len(strs[0])

        for element in strs:
            minimum = min(minimum,len(element))

        
        i = 0

        #strs[0] -> "flower"
        #strs[0][i] ->"f" ....."l" ..... "o" ..... 

        while(i<minimum):
            firstElementInStrs = strs[0][i] #it is "f" of "flower"
            for element in strs:
                if element[i] == firstElementInStrs:
                    continue
                else:
                    return strs[0][0:i]

            i+=1

        return strs[0][0:minimum]

                
            
            


        



            