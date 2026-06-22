class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n= len(matrix[0])
        for i in range (len(matrix)):
            if matrix[i][0]<target and matrix[i][n-1] and target in matrix[i]:
                return True
        return False
        