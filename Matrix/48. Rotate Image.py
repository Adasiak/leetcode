from copy import deepcopy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp = []
        for row in matrix:
            row_copy = deepcopy(row)
            tmp.append(row_copy)
        for i, mm in enumerate(reversed(tmp)):
            for j, char in enumerate(mm):
                matrix[j][i] = char
        
        return matrix
    
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. Transpozycja macierzy
        for i in range(n):
            for j in range(i, n):  # Zaczynamy od 'i' aby uniknąć podwójnej zamiany
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Odwrócenie każdego wiersza
        for i in range(n):
            matrix[i].reverse() # Wbudowana metoda reverse() jest efektywna