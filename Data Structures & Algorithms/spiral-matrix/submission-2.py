class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rowbegin, rowend = 0, n - 1
        colbegin, colend = 0, m - 1
        res = []

        while rowbegin <= rowend and colbegin <= colend:
            # Traverse top row
            for i in range(colbegin, colend + 1):
                res.append(matrix[rowbegin][i])
            rowbegin += 1

            # Traverse right column
            for i in range(rowbegin, rowend + 1):
                res.append(matrix[i][colend])
            colend -= 1

            # Traverse bottom row (if still within bounds)
            if rowbegin <= rowend:
                for i in range(colend, colbegin - 1, -1):
                    res.append(matrix[rowend][i])
                rowend -= 1

            # Traverse left column (if still within bounds)
            if colbegin <= colend:
                for i in range(rowend, rowbegin - 1, -1):
                    res.append(matrix[i][colbegin])
                colbegin += 1

        return res
