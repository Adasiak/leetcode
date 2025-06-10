from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))   # 1-based
        self.size   = [1]*(n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # spłaszczanie
        return self.parent[x]

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra]  += self.size[rb]

def getVisibleProfilesCount(nodes: int,
                            u: List[int],
                            v: List[int],
                            queries: List[int]) -> List[int]:
    dsu = DSU(nodes)

    # 1. scalaj krawędzie
    for a, b in zip(u, v):
        dsu.union(a, b)

    # 2. odpowiedzi
    ans = []
    for q in queries:
        root = dsu.find(q)
        ans.append(dsu.size[root])
    return ans


from typing import List

# ─────────── DSU (Disjoint-Set Union) ───────────
class DSU:
    def __init__(self, n: int):
        # parent[i] = i  → każdy węzeł jest własnym korzeniem
        self.parent = list(range(n + 1))        # indeksy 1..n
        # size[i] = liczba węzłów w komponencie z korzeniem i
        self.size   = [1] * (n + 1)

    def find(self, x: int) -> int:
        # path-compression: spłaszczamy drzewo w drodze do korzenia
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)     # korzenie obu węzłów
        if ra == rb:                            # już w jednym zbiorze
            return
        # union-by-size: mniejszy komponent podpinamy pod większy
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra                     # zamiana, by ra był większy
        self.parent[rb] = ra                    # korzeń rb wskazuje na ra
        self.size[ra]  += self.size[rb]         # aktualizacja rozmiaru


# ─────────── Główna funkcja ───────────
def getVisibleProfilesCount(nodes: int,
                            u: List[int],
                            v: List[int],
                            queries: List[int]) -> List[int]:
    dsu = DSU(nodes)                            # struktura do scalania

    # 1. scal wszystkie krawędzie grafu
    for a, b in zip(u, v):
        dsu.union(a, b)

    # 2. odpowiedz na każde zapytanie
    ans: List[int] = []
    for q in queries:
        root = dsu.find(q)                      # korzeń komponentu użytkownika q
        ans.append(dsu.size[root])              # rozmiar = liczba widocznych profili
    return ans




class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        
def getVisibleProfilesCount(nodes: int,
                            u: List[int],
                            v: List[int],
                            queries: List[int]) -> List[int]:  
        dsu = DSU(nodes)
        for a, b in zip(a, b):
            dsu.union(a, b)
        ans = []
        for q in queries:
            root = dsu.find(q)
            ans.append(dsu.size[root])
        return ans
    
    
    
    
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return 
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

def getVisibleProfilesCount(nodes: int,
                            u: List[int],
                            v: List[int],
                            queries: List[int]) -> List[int]: 
    dsu = DSU(nodes)
    
    for a, b in zip(a, b):
        dsu.union(a, b)
    ans = []
    for q in queries:
        root = dsu.find(q)
        ans.append(dsu.size[root])
    return ans







class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        for a, b in zip(a, b):
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        
def getVisibleProfilesCount(nodes: int,
                            u: List[int],
                            v: List[int],
                            queries: List[int]) -> List[int]: 
    dsu = DSU(nodes)
    for a, b in zip(a, b):
        dsu.union(a, b)
    ans = []
    for q in queries:
        root = dsu.find(q)
        ans.append(dsu.size[root])
    return ans