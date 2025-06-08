
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # pass
        if not node:
            return None
        clone = Node(node.val)
        clone_map = {node: clone}
        queue = [node]
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_map[curr].neighbors.append(clone_map[neighbor])
        return clone
    
    
    
# ─────────  DEKLARACJA WĘZŁA  ─────────────────────────────────────────────
class Node:                                                  # ❶
    def __init__(self, val = 0, neighbors = None):           # ❷
        self.val = val                                       # ❸
        self.neighbors = neighbors if neighbors is not None else []  # ❹


# ─────────  BIBLIOTEKA TYPÓW (tylko dla adnotacji)  ────────
from typing import Optional                                  # ❺


# ─────────  ROZWIĄZANIE  ───────────────────────────────────
class Solution:                                              # ❻
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:                      # ❽
        # 1. Graf pusty? ────────────────────────────────────
        if not node:                                         # ❾
            return None                                      # ❿

        # 2. Tworzymy klon startowego węzła ────────────────
        clone = Node(node.val)                               # ⓫

        # 3. Słownik ORYGINAŁ → KLON ───────────────────────
        clone_map = {node: clone}                            # ⓬

        # 4. Kolejka BFS (lista) z węzłem początkowym ──────
        queue = [node]                                       # ⓭

        # 5. Główna pętla BFS ──────────────────────────────
        while queue:                                         # ⓮
            curr = queue.pop(0)                              # ⓯

            # 5a. Iterujemy po sąsiadach oryginału
            for neighbor in curr.neighbors:                  # ⓰
                # 5b. Jeśli sąsiad N I E był jeszcze klonowany
                if neighbor not in clone_map:                # ⓱
                    clone_map[neighbor] = Node(neighbor.val) # ⓲
                    queue.append(neighbor)                   # ⓳

                # 5c. Łączymy klony: curr  →  neighbor
                clone_map[curr].neighbors.append(            # ⓴
                    clone_map[neighbor])

        # 6. Zwracamy klon korzenia ────────────────────────
        return clone                                         # ⓵





class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = Node(node.val)
        clone_map = {node: clone}
        queue = [node]
        while queue:
            curr = queue.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    queue.append(nei)
                
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone
    
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        clone = Node(node.val)
        clone_map = {node : clone}
        que = [node]
        while que:
            curr = que.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    que.append(nei)
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone
    
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = Node(node.val)
        clone_map = {node: clone}
        que = [node]
        while que:
            curr = que.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    que.append(nei)
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(node.val)
        clone_map = {node: clone}
        que = [node]
        while que:
            curr = que.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    que.append(nei)
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone
    
    
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(node.val)
        clone_map = {node: clone}
        que = [node]
        while que:
            curr = que.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    que.append(nei)
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone
    
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(node.val)
        clone_map = {node: clone}
        q = [node]
        while q:
            curr = q.pop(0)
            for nei in curr.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    q.append(nei)
                clone_map[curr].neighbors.append(
                    clone_map[nei]
                )
        return clone