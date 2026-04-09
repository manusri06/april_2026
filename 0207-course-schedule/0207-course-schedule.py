class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            course = q.popleft()
            count+=1
            for nei in g[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return count == numCourses

