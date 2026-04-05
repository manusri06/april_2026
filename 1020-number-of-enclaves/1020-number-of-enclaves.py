class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        for r in range(row):
            dfs(r, 0)
            dfs(r, col-1)
        for c in range(1,col-1):
            dfs(0, c)
            dfs(row-1, c)
        
        count = 0
        for i in grid:
            for j in i:
                if j == 1:
                    count+=1
        return count