from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        
        direction = [(-1,0),(0,-1),(1,0),(0,1),(1,-1),(-1,1),(1,1),(-1,-1)]
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1

        while q:
            r, c, s = q.popleft()
            if r == row-1 and c == col-1:
                return s
            for i, j in direction:
                nr, nc = r+i, c+j
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 0:
                        q.append((nr, nc, s+1))
                        grid[nr][nc] = 1
        return -1