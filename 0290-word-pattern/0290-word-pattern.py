class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = []

        words = s.split()

        d = {}

        n = len(pattern)
        n1 = len(words)

        if n != n1:
            return False

        for i in range(0,n):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i] 

        return True



        

        