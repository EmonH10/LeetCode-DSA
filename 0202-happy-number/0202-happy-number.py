class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while(n != 1):  

            if n in seen:
                return False
            
            seen.add(n)

            res = 0
            while(n>0):
                r = n%10
                res += (r*r) 
                n = n//10

            if res == 1:
                return True

            n = res

        return True


        