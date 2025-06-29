"""
BFS – Breadth-First Search (pol. przeszukiwanie wszerz)
Algorytm eksploruje graf poziomami: 
najpierw wszystkie węzły w odległości 1 od startu, 
potem 2, 3 … Dzięki temu najwcześniej znalezioną ścieżką 
jest zawsze ta o najmniejszej liczbie krawędzi.

DFS – Depth-First Search (pol. przeszukiwanie wgłąb)
Algorytm zagłębia się maksymalnie w jedną gałąź grafu/drzewa, 
zanim się wycofa (backtracking) i spróbuje kolejnej ścieżki. 
Używa stosu (rekurencyjnie lub iteracyjnie).
"""


# === BFS (graf nieskierowany) =========================================
from collections import deque
from typing import List, Dict, Set

def bfs(start: int, adj: Dict[int, List[int]]) -> Dict[int, int]:
    """
    start  – wierzchołek początkowy
    adj    – lista sąsiedztwa {wierzchołek: [sąsiedzi]}

    Zwraca słownik dist  {w: najkrótsza liczba krawędzi od start do w}.
    """
    q: deque[int] = deque([start])   # kolejka do przetwarzania wierzchołków
    visited: Set[int] = {start}      # już odwiedzone wierzchołki
    dist: Dict[int, int] = {start: 0}

    while q:
        v = q.popleft()              # zdejmij z kolejki
        for nei in adj[v]:           # przejrzyj sąsiadów
            if nei not in visited:   # jeśli jeszcze nie widziany…
                visited.add(nei)     # …oznacz jako odwiedzony
                dist[nei] = dist[v] + 1  # aktualizuj dystans
                q.append(nei)        # dodaj do kolejki
    return dist                      # mapa najkrótszych odległości


# === BFS (siatka - 4 kierunki) ========================================
DIRS = [(1,0), (-1,0), (0,1), (0,-1)]   # ruchy: dół, góra, prawo, lewo

def bfs_grid(sr: int, sc: int, grid: List[List[str]]) -> Set[tuple[int,int]]:
    """
    sr, sc  – współrzędne startowe (wiersz, kolumna)
    grid    – macierz znaków '1' (ląd) / '0' (woda)

    Zwraca zbiór komórek lądu, do których dotrzemy z (sr, sc).
    """
    R, C = len(grid), len(grid[0])
    q = deque([(sr, sc)])
    seen = {(sr, sc)}

    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            inside = 0 <= nr < R and 0 <= nc < C
            if inside and grid[nr][nc] == '1' and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc))
    return seen


# === DFS (rekurencyjny) ==============================================
def dfs(v: int, adj: Dict[int, List[int]], visited: Set[int]) -> None:
    """
    Standardowy DFS rekurencyjny – odwiedza wszystkie wierzchołki
    w tej samej składowej co v.
    """
    visited.add(v)
    for nei in adj[v]:
        if nei not in visited:
            dfs(nei, adj, visited)


# === DFS (iteracyjny – stos) =========================================
def dfs_iter(start: int, adj: Dict[int, List[int]]) -> Set[int]:
    """
    Iteracyjna wersja DFS – bez ryzyka przepełnienia stosu Pythona.
    Zwraca zbiór odwiedzonych wierzchołków.
    """
    stack: list[int] = [start]
    visited: Set[int] = set()

    while stack:
        v = stack.pop()
        if v in visited:
            continue          # już był – pomijamy
        visited.add(v)
        stack.extend(adj[v])  # wrzucamy sąsiadów na stos
    return visited


# === 1-D Dynamic Programming – Coin Change ===========================
def coinChange(coins: List[int], amount: int) -> int:
    """
    coins  – dostępne nominały monet
    amount – docelowa kwota

    Zwraca minimalną liczbę monet lub -1, jeśli nieosiągalne.
    """
    if amount == 0:
        return 0
    if not coins:
        return -1

    INF = 10**12
    dp = [INF] * (amount + 1)
    dp[0] = 0                       # baza: 0 monet, by uzyskać 0

    # zewnętrzna pętla po monetach (każdą monetę możemy używać wielokrotnie)
    for coin in coins:
        # zaczynamy od wartości coin, by nie wychodzić poza tablicę (i-coin >= 0)
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == INF else dp[amount]


# === Min-heap (k najmniejszych) ======================================
import heapq

def k_smallest(nums: List[int], k: int) -> List[int]:
    """
    Zwraca listę k najmniejszych liczb z nums (kolejność kopca).
    """
    heapq.heapify(nums)                       # zamiana listy w kopiec w O(n)
    return [heapq.heappop(nums) for _ in range(k)]  # k razy pop w O(k log n)


# === Max-heap (negacja wartości) =====================================
def max_heap_push(heap: list[int], val: int) -> None:
    """Wstaw wartość do kopca maksymalnego (przechowujemy ujemne)."""
    heapq.heappush(heap, -val)

def max_heap_pop(heap: list[int]) -> int:
    """Wyjmij największą wartość z kopca maksymalnego."""
    return -heapq.heappop(heap)
