class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        #Convert it to Binary 

        result = []

        while(n>0):

            result.append(n%2)

            n = n//2

        
        count = 0

        for i in result:

            if i == 1:
                count += 1

        if count == 1:
            return True 

        return False