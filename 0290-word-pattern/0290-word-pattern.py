class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = []

        i = 0
        while(i<len(s)):

            element = ""

            while i<len(s) and s[i] != " ":
                element += s[i]
                i+=1
            words.append(element)

            i+=1

        if len(words) != len(pattern):
            return False

        d = {}

        for i in range(0,len(pattern)):

            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]

        return True

        

        