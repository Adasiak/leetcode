from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return 0
        corner = set()
        # first = edges[0][0]
        for con in edges:
            if con[0] in corner and con[1] in corner:
                return con
            else:
                # if con[0] != first:
                corner.add(con[0])
                corner.add(con[1])
                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        parent = {}                 # ➊ zamiast set() – słownik „tata” w DSU

        def find(x):
            parent.setdefault(x, x)   # jeśli brak wpisu, wpisz „sam siebie”
            if parent[x] != x:        # jeśli klocek trzyma kogoś innego…
                parent[x] = find(parent[x])  # …idź dalej za rączki do samego króla
            return parent[x]          # oddaj numer króla


        for u, v in edges:
            ru, rv = find(u), find(v)   # królowie klocków u i v
            if ru == rv:                # już mają tego samego króla ⇒ są w jednej paczce
                return [u, v]           # ten sznurek zrobił pętelkę — oddajemy go
            parent[rv] = ru             # inaczej: przywiąż paczkę v do paczki u



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return 0
        parrent = {}
        def find(x):
            parrent.setdefault(x, x)
            if parrent[x] != x:
                parrent[x] = find(parrent[x])
            return parrent[x]
        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]
            parrent[rv] = ru