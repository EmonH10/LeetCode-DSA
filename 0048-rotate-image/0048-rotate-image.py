class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


        print(matrix)

        n = len(matrix)
        for i in range(0,n):

            j = n-1
            low = 0
            while(low<j):
                matrix[i][low],matrix[i][j] = matrix[i][j],matrix[i][low]
                low+=1
                j-=1 


        