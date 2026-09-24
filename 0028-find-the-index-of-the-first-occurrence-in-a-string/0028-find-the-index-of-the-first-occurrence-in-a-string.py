class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(needle)

        for i in range(0,len(haystack)-n+1):
            j = i
            element = ""
            while(j<i+n):
                element += haystack[j]
                j+=1

            if element == needle:
                return i

        return -1



        