class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        colums=len(grid[0])
        count=0
        
        def dfs(grid,r,c):
            if r<0 or r>= len(grid) or c<0 or c >= colums or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(grid,r,c-1)
            dfs(grid,r,c+1)
            dfs(grid,r+1,c)
            dfs(grid,r-1,c)
        for i in range (rows):
            for j in range (colums):
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    count+=1
        return count
        