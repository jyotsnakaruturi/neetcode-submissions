class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        r=len(matrix)
        c=len(matrix[0])
        for i in range (r):
            for j in range (i+1,c):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        

        