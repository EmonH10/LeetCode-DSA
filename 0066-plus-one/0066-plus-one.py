class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        result = 0

        for i in digits:
            result = result*10 + i

        result = result + 1

        new = []

        while(result>0):
            new.append(result%10)

            result = result//10

        i = 0
        j = len(new)-1

        while(i<j):
            new[i],new[j] = new[j],new[i]
            i+=1
            j-=1

        return new        