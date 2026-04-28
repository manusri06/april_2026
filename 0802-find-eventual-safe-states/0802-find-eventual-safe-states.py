from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [0]*n
        adj = defaultdict(list)

        for i in range(n):
            outdeg[i] = len(graph[i])
            for j in graph[i]:
                adj[j].append(i)    
        ans = []
        q = deque()
        for i in range(n):
            if outdeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                outdeg[nei] -= 1
                if outdeg[nei] == 0:
                    q.append(nei)
        return sorted(ans)
        
