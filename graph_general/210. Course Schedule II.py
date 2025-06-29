from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        indeg = [0]*numCourses
        
        for next, pre in prerequisites:
            G[pre].append(next)
            indeg[next] += 1
        
        q = deque([i for i, deg in enumerate(indeg) if deg == 0])
        res = []
        while q:
            v = q.popleft()
            res.append(v)
            for nei in G[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []