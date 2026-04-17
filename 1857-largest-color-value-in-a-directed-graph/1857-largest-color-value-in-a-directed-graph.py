from collections import deque, defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        indg = [0]*(len(colors))
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            indg[v] += 1

        q = deque()
        dp = [[0]*26 for _ in range(len(colors))]

        for i in range(len(indg)):
            if indg[i] == 0:
                q.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1
        ans = 0
        visited = 0

        while q:
            node = q.popleft()
            visited += 1
            ans = max(ans, max(dp[node]))

            for nei in g[node]:
                nei_color = ord(colors[nei]) - ord('a')
                for c in range(26):
                    if c == nei_color:
                        dp[nei][c] = max(dp[nei][c], dp[node][c] + 1)
                    else:
                        dp[nei][c] = max(dp[nei][c], dp[node][c])

                indg[nei] -= 1
                if indg[nei] == 0:
                    q.append(nei)
                
        return ans if visited == len(colors) else -1
