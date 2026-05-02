class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,colms=len(matrix),len(matrix[0])
        rowzero=False

        for i in range (row):
            for j in range (colms):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        rowzero=True
        for i in range (1,row):
            for j in range (1,colms):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range (row):
                matrix[i][0]=0
        if rowzero:
            for j in range (colms):
                matrix[0][j]=0


        
        