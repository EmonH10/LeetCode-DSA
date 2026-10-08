class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        column = n-1

        while(row<m and column>=0):

            if matrix[row][column] == target:
                return True

            elif matrix[row][column] >target:
                column -= 1
            else:
                row += 1

        return False
        