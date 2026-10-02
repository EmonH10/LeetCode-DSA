class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        low = 0
        high = 0
        length = 0
        maxlength = 0

        for i in range(0,len(s)):
            if s[i] in freq and low<=freq[s[i]]:
                high += 1
                low = freq[s[i]]+1
                freq[s[i]] = i
                length = high-low
            else:
                high += 1
                freq[s[i]] = i
                length = high-low

            maxlength = max(maxlength,length)

        return maxlength
        
        