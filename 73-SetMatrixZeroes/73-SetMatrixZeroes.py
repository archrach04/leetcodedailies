# Last updated: 3/28/2026, 12:55:26 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        columns=len(matrix[0])
        rows=len(matrix)
        firstRow = False
        firstCol = False

        # check first row
        for j in range(columns):
            if matrix[0][j] == 0:
                firstRow = True

        # check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                firstCol = True
        for i in range(1,rows):
            for j in range(1,columns):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,rows):
            for j in range(1,columns):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if firstRow:
            matrix[0] = [0] * columns

        if firstCol:
            for i in range(rows):
                matrix[i][0] = 0
        





        