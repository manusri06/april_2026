from collections import deque
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row = len(grid)
        col = len(grid[0])

        visited = [[False]*col for _ in range(row)]

        def dfs(r, c, pr, pc, ch):

            visited[r][c] = True
            directions = [(0,1),(1,0),(-1,0),(0,-1)]

            for i, j in directions:
                nr, nc = r+i, c+j
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == ch:
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, ch):
                            return True
                    elif (nr, nc) != (pr, pc):
                        return True

        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False
                    

