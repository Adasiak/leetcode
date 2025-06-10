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
