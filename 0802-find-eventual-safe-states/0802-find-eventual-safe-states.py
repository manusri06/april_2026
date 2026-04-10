from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        outdegree = [0]*V
        g = defaultdict(list)
        
        for u in range(V):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                g[v].append(u)

        q = deque()
        for i in range(V):
            if outdegree[i] == 0:
                q.append(i)
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for nei in g[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    q.append(nei)

        return sorted(result)

