class Solution:
    def compress(self, strs: List[str]) -> int:
        n = len(strs)
        i = 0
        j = 0

        while(i<n):
            element = strs[i]
            count = 0
            while(i<n and element == strs[i]):
                count += 1
                i+=1

            strs[j] = element
            j+=1
            if count>1 and count<10:
                strs[j] = str(count)
                j+=1
            if count>9:
                count = str(count)
                for element in count:
                    strs[j] = element
                    j += 1

        return j