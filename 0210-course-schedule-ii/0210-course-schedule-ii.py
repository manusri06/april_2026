from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return topo if len(topo) == numCourses else [] 

        """ indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(ans) != numCourses:
            return []
        
        return ans
 """