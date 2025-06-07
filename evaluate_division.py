from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. budujemy graf nieważony
        G = defaultdict(list)           # wierzchołek -> lista (sąsiad, waga)
        for (a, b), k in zip(equations, values):
            G[a].append((b, k))
            G[b].append((a, 1.0 / k))
        def bfs(src: str, dst: str) -> float:
            if src not in G or dst not in G:
                return -1.0
            if src == dst:
                return 1.0
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                v, acc = q.popleft()
                if v == dst:
                    return acc
                for nei, w in G[v]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, acc * w))
            return -1.0
        # 2. obsługa zapytań
        return [bfs(a, b) for a, b in queries]


def calEquation(eq, val, que):
    G = defaultdict(list)
    for (a, b) , k in zip(eq, val):
        G[a].append((b, k))
        G[b].append((a, 1.0 / k))
    def bfs(src, dst):
        if src not in G or dst not in G:
            return -1
        if src == dst:
            return 1
        
        q = deque([(src, 1.0)])
        seen  = {src}
        while q:
            v, acc = q.popleft()
            if v == dst:
                return acc
            for nei, w in G[v]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, acc * w))
        return -1.0
    return [bfs(a, b) for a, b in que]



def calEquities(eq, val, que):
    g = defaultdict(list)
    for (a, b), k in zip(eq, val):
        g[a].append((b, k))
        g[b].append((a, 1.0/k))
    
    def bfs(src, dst):
        if src not in g or dst not in g:
            return -1.0
        if src == dst:
            return 1.0
        
        q = deque([(src, 1.0)])
        seen = {src}
        
        while q:
            v, acc = q.popleft()
            if v == dst:
                return acc
            for nei, w in g[v]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, acc * w))
        return -1.0 
    
    return [bfs(a, b) for a, b in que]





def calcEq(eq, val, que):
    g = defaultdict(list)
    for (a, b) , k in zip(eq, val):
        g[a].append((b, k))
        g[b].append((a, 1 / k))
    
    def bfs(src, dst):
        if src not in g or dst not in g:
            return -1
        if src == dst:
            return 1
        
        q = deque([(src, 1.0)])
        seen = {src}
        while q:
            v, acc = q.popleft()
            if v == dst:
                return acc
            
            for nei, w in g[v]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, acc * w))
        return -1.0
    
    return [bfs(a, b) for a, b in que]
            


