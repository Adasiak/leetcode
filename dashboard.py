# === BFS (graph) ===
from collections import deque
from typing import List
def bfs(start, adj):
    q = deque([start])
    visited = {start}
    dist = {start: 0}
    while q:
        v = q.popleft()
        for nei in adj[v]:
            if nei not in visited:
                visited.add(nei)
                dist[nei] = dist[v] + 1
                q.append(nei)
    return dist

# === BFS (grid 4■dir) ===
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs_grid(sr, sc, grid):
    R, C = len(grid), len(grid[0])
    q = deque([(sr, sc)])
    seen = {(sr, sc)}
    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1' and (nr,nc) not in seen:
                seen.add((nr,nc)); q.append((nr,nc))
    return seen

# === DFS (recursive) ===
def dfs(v, adj, visited):
    visited.add(v)
    for nei in adj[v]:
        if nei not in visited:
            dfs(nei, adj, visited)

# === DFS (iterative) ===
def dfs_iter(start, adj):
    stack = [start]; visited = set()
    while stack:
        v = stack.pop()
        if v in visited: 
            continue
        visited.add(v)
        stack.extend(adj[v])
    return visited

# === 1■D DP template ===
def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0 :
        return 0
    if not coins:
        return -1
    INF = 10**12
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == INF else dp[amount]

# === Min■heap template ===
import heapq
def k_smallest(nums, k):
    heapq.heapify(nums) # O(n)
    return [heapq.heappop(nums) for _ in range(k)]

# Max■heap via negation:
def max_heap_push(heap, val):
    heapq.heappush(heap, -val)
def max_heap_pop(heap):
    return -heapq.heappop(heap)