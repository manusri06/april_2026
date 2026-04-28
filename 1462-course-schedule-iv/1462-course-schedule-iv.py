from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indeg = defaultdict(list)
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
        
        return ans

        

        