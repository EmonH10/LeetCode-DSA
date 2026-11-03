class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}
        c = ""

        for i in range(0,len(s)):

            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        for element in freq:

            if freq[element] == 1:
                c += element
                break

        for i in range(0,len(s)):
            if s[i] == c:
                return i

        return -1
            