class Solution:
    def reverse(self, x: int) -> int:

        sign = 1

        if x < 0:
            x = x*-1
            sign = -1

        temp = 0

        while(x>0):
            temp = temp*10
            temp = temp + x%10
            x = x//10

        if temp < -(2**31) or temp >= (2**31 - 1):
            return 0

        return temp*sign

        
        