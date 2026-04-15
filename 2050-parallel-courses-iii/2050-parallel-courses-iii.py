from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg = [0]*(n+1)
        g = defaultdict(list)

        for u, v in relations:
            g[u].append(v)
            indeg[v] += 1
        
        q = deque()
        dp = [0]*(n+1)

        for i in range(1,n+1):
            if indeg[i] == 0:
                q.append(i)
                dp[i] = time[i-1]

        while q:
            node = q.popleft()
            for nei in g[node]:
                dp[nei] = max(dp[nei], dp[node] + time[nei-1])
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return max(dp)



