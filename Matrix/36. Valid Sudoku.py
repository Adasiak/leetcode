from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(listt: List[str]):
            n = listt.count(".")
            expected_numbers = len(listt) - n
            if expected_numbers != len(set(listt)) - 1:
                # print(expected_numbers, len(set(listt)) - 1)
                return False
            else:
                return True
        
        def matrix(x, y):
            tmp = []
            for i in range(3):
                for j in range(3):
                    tmp.append(board[x+i][y+j])
            # print(tmp)
            return validate(tmp)
        
        for row in board:
            if not validate(row):
                # print("row", row)
                return False
        
        for i in range(len(board)):
            tmp = [board[x][i] for x in range(len(board))]
            if not validate(tmp):
                # print("col", tmp)
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not matrix(i, j):
                    # print("matrix", i, j)
                    return False
        
        return True
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num=='.':
                    continue
                box_index=(i//3)*3+(j//3)
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        return True 
    
    
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box_index = (i//3)*3+(j//3)
                if num in rows[i] or num in cols[i] or num in boxes[box_index]:
                    return False
                rows[i].add(num)
                cols[i].add(num)
                boxes[box_index].add(num)
        return True