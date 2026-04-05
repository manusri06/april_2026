from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    q.append((i, j))

        if not q or len(q) == row*col:
            return -1

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        distance = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1   
                        q.append((nr, nc))

            distance += 1
        return distance