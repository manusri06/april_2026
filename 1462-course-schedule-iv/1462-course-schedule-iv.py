from collections import defaultdict,deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indeg = [0]*numCourses
        adj = defaultdict(list)

        for i, j in prerequisites:
            adj[i].append(j)
            indeg[j] += 1
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        conn = [set() for _ in range(numCourses)]
        while q:
            node = q.popleft()
            
            for nei in adj[node]:
                conn[nei].add(node)
                conn[nei].update(conn[node])

                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return [i in conn[j] for i, j in queries]

        """ indeg = defaultdict(list)
        for i, j in prerequisites:
            indeg[i].append(j)

        memo = {}
        def dfs(src, target):
            if target == src:
                return True

            if (src, target) in memo:
                return memo[src, target]

            for nei in indeg[src]:
                if dfs(nei, target):
                    memo[(src, target)] = True
                    return True
            memo[(src, target)] = False
            return False

        ans = []
        for i, j in queries:
            ans.append(dfs(i, j))
        
        return ans """

        

        