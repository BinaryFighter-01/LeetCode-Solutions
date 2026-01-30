from typing import List

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        INF = 10**15
        
        # dist[i][j] = min cost to convert chr(i+'a') → chr(j+'a')
        dist = [[INF] * 26 for _ in range(26)]
        
        # same character costs 0
        for i in range(26):
            dist[i][i] = 0
        
        # direct conversions
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd–Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # compute answer
        ans = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        
        return ans
