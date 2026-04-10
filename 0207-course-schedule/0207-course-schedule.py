from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1

        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        taken = 0
        while q:
            node = q.popleft()
            taken += 1
        
            for nei in g[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return taken == numCourses



        

