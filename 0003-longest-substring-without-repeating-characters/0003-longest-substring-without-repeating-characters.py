class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq = {}
        low = 0
        high = 0
        length = 0
        maximum = 0

        for i in range(0,len(s)):

            if s[i] in freq and low<=freq[s[i]]:
                low = freq[s[i]]+1
                freq[s[i]] = i
                high += 1
                length = high-low
            else:
                freq[s[i]] = i
                high += 1
                length = high-low

            maximum = max(maximum,length)

        return maximum

        