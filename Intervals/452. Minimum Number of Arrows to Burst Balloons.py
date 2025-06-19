from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda p: p[1])
        arrows = 0
        shoot_pos = float('-inf')

        # 2) greedy
        for start, end in points:
            if start > shoot_pos:
                arrows += 1          # nowa strzała
                shoot_pos = end      # ustawiamy pozycję strzału na koniec bieżącego balonu

        return arrows
    
    
    
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:   
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 0
        shooting_point = float("-inf")
        
        for start, end in points:
            if start > shooting_point:
                shooting_point = end
                arrows += 1
        return arrows
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:   
        if not points:
            return 0 
        points.sort(key=lambda p:p[1])
        arrows = 0
        shooting_point = float("-inf")
        for start, end in points:
            if start > shooting_point:
                arrows += 1
                shooting_point = end
        return arrows
    
    
    
    
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:   
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 0
        shooting_point = float("-inf")
        for start, end in points:
            if start > shooting_point:
                arrows += 1
                shooting_point = end
        return arrows