class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res1 = 0
        for i in a:
            i = int(i)
            res1 = res1*2 + i

        res2 = 0
        for i in b:
            i = int(i)
            res2 = res2*2 + i

        res = res1+res2

        s = ""
        while(res != 0):
            s += str(res%2)
            res = res//2

        if s == "":
            return "0"
            
        return s[::-1]

        