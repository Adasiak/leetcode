from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        G = defaultdict(list)
        indeg = [0]*numCourses
        for nxt, pre in prerequisites:
            G[pre].append(nxt)
            indeg[nxt] += 1

        q = deque([i for i,deg in enumerate(indeg) if deg==0])
        visited = 0
        while q:
            v = q.popleft()
            visited += 1
            for nei in G[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return visited == numCourses
    
    
def canFinish(number_of_courses, prerequisites):
    from collections import defaultdict, deque
    G = defaultdict(list)
    indeg = [0] * number_of_courses
    for next, pre in prerequisites:
        G[pre].append(next)
        indeg[next] +=1
    
    q = deque([i for i, deg in enumerate(indeg) if deg ==0])
    visited = 0
    while q:
        v = q.popleft()
        visited += 1
        for nei in G[v]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return visited == number_of_courses



def canFinish(number_of_courses, polozenie):
    from collections import defaultdict, deque
    
    G = defaultdict(list)
    ilosc_wartosci_wstepnych = [0] * number_of_courses
    
    for next, pre in polozenie:
        G[pre].append(next)
        ilosc_wartosci_wstepnych[next] += 1
    q = deque([i for i, deg in enumerate(ilosc_wartosci_wstepnych) if deg == 0])
    
    visited = 0
    while q:
        v = q.popleft()
        visited +=1
        
        for sasiad in G[v]:
            ilosc_wartosci_wstepnych[sasiad] -= 1
            if ilosc_wartosci_wstepnych[sasiad] == 0:
                q.append(sasiad)
    return visited == number_of_courses
    
def canFinish(numbers_of_courses, polozenie):
    from collections import defaultdict, deque
    
    G = defaultdict(list)
    ilosc_wartosci_wstepnych = [0] * numbers_of_courses
    
    for next, pre in polozenie:
        G[pre].append(next)
        ilosc_wartosci_wstepnych[next] += 1 
    
    q = deque([i for i, d in enumerate(ilosc_wartosci_wstepnych) if d == 0])
    
    visited = 0
    while q:
        v = q.popleft()
        visited += 1
        
        for sasiad in G[v]:
            ilosc_wartosci_wstepnych[sasiad] -= 1
            if ilosc_wartosci_wstepnych[sasiad] == 0:
                q.append(sasiad)
    return visited == numbers_of_courses









def canFinish( numbers_of_steps, wspolzedne):
    from collections import defaultdict, deque
    
    G = defaultdict(list)
    
    ilosc_pozostalych  = [0] * numbers_of_steps
    
    for next, pre in wspolzedne:
        G[pre].append(next)
        ilosc_pozostalych[next] +=1
    q = deque([i for i, d in enumerate(ilosc_pozostalych) if d == 0])
    visited = 0
    while q:
        v = q.popleft()
        visited += 1
        for neib in G[v]:
            ilosc_pozostalych[neib] -= 1
            if ilosc_pozostalych[neib] == 0:
                q.append(neib)
    return visited == numbers_of_steps



def can_finish(number_of_steps, cordination):
    from collections import defaultdict, deque
    
    G = defaultdict(list)
    left_coordination = [0] * number_of_steps
    for next, pre in cordination:
        G[pre].append(next)
        left_coordination[next] += 1
    q = deque([i for i, d in enumerate(left_coordination) if d == 0])
    visited = 0
    while q:
        visited += 1
        v = q.popleft()
        for nei in G[v]:
            left_coordination[nei] -= 1
            if left_coordination[nei] == 0:
                q.append(nei)
    return visited == number_of_steps
        
        


def canFinish(number_of_steps, coordination) -> bool:
    from collections import defaultdict, deque
    G = defaultdict(list)
    left_coordination = [0] * number_of_steps
    
    for next, pre in coordination:
        G[pre].append(next)
        left_coordination[next] += 1
    
    q = deque([i for i, d in enumerate(left_coordination) if d == 0])
    visited = 0
    while q:
        visited += 1
        v = q.popleft()
        
        for nei in G[v]:
            left_coordination[nei] -= 1
            if left_coordination[nei] == 0:
                q.append(nei)
    return visited == number_of_steps




def canFinish(number_of_steps, coordination):
    from collections import defaultdict, deque
    G = defaultdict(list)
    left_coordination = [0]*number_of_steps
    for next, pre in coordination:
        G[pre].append(next)
        left_coordination[next] += 1
    q = deque([i for i, d in enumerate(left_coordination) if d == 0])
    visited = 0
    
    while q:
        v = q.popleft()
        visited += 1
        for nei in G[v]:
            left_coordination[nei] -= 1
            if left_coordination[nei] == 0:
                q.append(nei)
    return visited == number_of_steps
    