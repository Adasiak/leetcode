from heapq import heappop, heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        g = [[] for _ in range(n)]
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))

        INF = 10**20
        dist = [INF]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]                    # (d, node)
        while pq:
            d, v = heapq.heappop(pq)
            if d > dist[v]: continue
            for nxt, w in g[v]:
                nd = d + w
                if nd < dist[nxt]:
                    dist[nxt], ways[nxt] = nd, ways[v]
                    heapq.heappush(pq, (nd, nxt))
                elif nd == dist[nxt]:
                    ways[nxt] = (ways[nxt] + ways[v]) % MOD
        return ways[n-1] % MOD
    
    
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        g = [[] for _ in range(n)]
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        
        INF = 10 ** 20
        
        dist = [INF] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, v = heappop(pq)
            
            if d > dist[v]:
                continue
            
            for next, w in g[v]:
                nd = d + w
                if nd < dist[next]:
                    dist[next], ways[next] = nd, ways[v]
                    heappush(pq, (nd, next))
                elif nd ==  dist[next]:
                    ways[next] = (ways[next] + ways[v]) % MOD
        return ways[n - 1] % MOD