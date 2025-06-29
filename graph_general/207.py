from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indeg = [0]*numCourses
        
        for next, pre in prerequisites:
            G[pre].append(next)
            indeg[next] += 1
        
        q = deque([i for i, deg in enumerate(indeg) if deg == 0])
        visited = 0
        while q:
            v = q.popleft()
            visited += 1
            for nei in G[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return visited == numCourses















    




class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indeg = [0]*numCourses
        
        for next, pre in prerequisites:
            G[pre].append(next)
            indeg[next] += 1
        
        q = deque([i for i, deg in enumerate(indeg) if deg == 0])
        visited = 0
        
        while q:
            v = q.popleft()
            visited += 1
            
            for nei in G[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return numCourses == visited





















    




























    















class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indeg = [0] * numCourses
        
        for next, pre in prerequisites:
            G[pre].append(next)
            indeg[next] += 1
        
        q = deque([i for i, deg in enumerate(indeg) if deg == 0])
        visited = 0
        while q:
            v = q.popleft()
            visited += 1 
            for nei in G[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return numCourses == visited