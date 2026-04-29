from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0]*n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaf = deque()
        for i in range(n):
            if degree[i] == 1:
                leaf.append(i)
        leaf_count = n

        while leaf_count > 2:
            nn = len(leaf)
            leaf_count -= nn

            for i in range(nn):
                l = leaf.popleft()
                for nei in graph[l]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaf.append(nei)
        return list(leaf)
