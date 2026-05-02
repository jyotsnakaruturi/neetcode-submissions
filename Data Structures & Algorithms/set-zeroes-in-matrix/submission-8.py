class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        rowzero=0
        for i in range (r):
            for j in range (c):
                if matrix[i][j] == 0:
                    matrix[0][j] =0
                    if i > 0:
                        matrix[i][0] =0
                    else:
                        rowzero = 1
        for i in range (1,r):
            for j in range (1,c):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] =0
        if matrix[0][0] == 0:
            for j in range (r):
                matrix[j][0] =0

        if rowzero == 1:
            for i in range (c):
                matrix[0][i] = 0
        
        
        