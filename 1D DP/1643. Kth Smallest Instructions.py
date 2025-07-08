from copy import deepcopy
from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        R, C = destination[0] + 1, destination[1] + 1
        
        dp = [[[]] * C for _ in range(R)]
        dp[0][0] = 0
        
        for i in range(R):
            for j in range(C):
                if i == 0:
                    ss_to_add = "H" * j
                    tmp = [ss_to_add]
                    dp[i][j] = tmp
                elif j == 0:
                    ss_to_add = "V" * i
                    tmp = [ss_to_add]
                    dp[i][j] = tmp
                else:
                    list_up = deepcopy(dp[i - 1][j])
                    for z in range(len(list_up)):
                        list_up[z] += "V"
                    list_left = deepcopy(dp[i][j - 1])
                    for q in range(len(list_left)):
                        list_left[q] += "H"
                    final_list = list_up + list_left
                    dp[i][j] = final_list
        res = dp[-1][-1]
        res.sort()
        return res[k-1]
    
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        import math

        # Możesz zaimplementować własną funkcję kombinacji,
        # jeśli nie chcesz polegać na math.comb lub jeśli chcesz ją zoptymalizować
        # dla małych N. Dla tego problemu math.comb jest wystarczające.
        # Zapamiętywanie wyników kombinacji (opcjonalne, math.comb jest zoptymalizowane)
        memo = {}
        def get_combinations(n, k):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            if k > n // 2: # optymalizacja C(n, k) = C(n, n-k)
                k = n - k
            if (n, k) in memo:
                return memo[(n, k)]

            # Obliczanie kombinacji, np. z math.comb
            res = math.comb(n, k)
            memo[(n, k)] = res
            return res
        
        
        
        result_path = []
        rows_to_go = destination[0]
        cols_to_go = destination[1]

        for _ in range(rows_to_go + cols_to_go): # Iteruj tyle razy, ile jest wszystkich kroków
            # Ile ścieżek zaczyna się od 'H' z obecnego stanu?
            # To jest liczba sposobów na wybranie pozostałych 'cols_to_go - 1' 'H'
            # z 'rows_to_go + cols_to_go - 1' pozostałych kroków.

            # Sprawdzamy, czy jeszcze możemy iść w prawo (H)
            if cols_to_go > 0:
                # Oblicz liczbę ścieżek, jeśli wybierzemy 'H' teraz.
                # Pozostałe kroki = (rows_to_go) + (cols_to_go - 1)
                # Musimy wybrać (cols_to_go - 1) ruchów 'H' spośród pozostałych.
                ways_if_H_next = get_combinations(rows_to_go + cols_to_go - 1, cols_to_go - 1)
            else:
                ways_if_H_next = 0 # Nie ma więcej ruchów 'H'

            # Podejmij decyzję:
            if k <= ways_if_H_next:
                # K-ta ścieżka jest wśród tych, które zaczynają się od 'H'.
                result_path.append('H')
                cols_to_go -= 1 # Zmniejsz liczbę pozostałych ruchów 'H'
                # K pozostaje bez zmian, bo nadal szukamy k-tej ścieżki w podgrupie 'H'
            else:
                # K-ta ścieżka nie zaczyna się od 'H', musi zaczynać się od 'V'.
                result_path.append('V')
                rows_to_go -= 1 # Zmniejsz liczbę pozostałych ruchów 'V'
                # Zaktualizuj K: odejmij liczbę ścieżek 'H', które pominęliśmy.
                k -= ways_if_H_next

        return "".join(result_path)
    
    
from math import comb
from typing import List

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination
        answer = []

        while row or col:
            if col == 0:            # zostały tylko V
                answer.append('V' * row)
                break
            if row == 0:            # zostały tylko H
                answer.append('H' * col)
                break

            count_H_first = comb(row + col - 1, row)   # ścieżki zaczynające się od 'H'

            if k <= count_H_first:
                answer.append('H')
                col -= 1
            else:
                answer.append('V')
                k -= count_H_first
                row -= 1

        return ''.join(answer)
    
    


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination
        res = []
        
        while col or row:
            if row == 0:
                res.append("H" * row)
                break
            
            elif col == 0:
                res.append("V" * col)
                break
            
            ss = comb(row + col - 1, row)
            if k <= ss:
                res.append("H")
                col -= 1
            else:
                res.append("V")
                k -= ss
                row -= 1
                
        return "".join(res)