from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights + [0]):   # dodatkowy 0 wymusza opróżnienie stosu
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                right = i #      (ten, na którym jesteś)
                left  = stack[-1] if stack else -1 # po popie     (jeśli pusty → left = -1)
                width = right - left - 1   #       (sprawdź na kartce!)
                area  = heights[top] * width
                if maxArea < area:
                    maxArea = area
            stack.append(i)
        return maxArea

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []                    # przechowuje *indeksy* słupków o rosnących wysokościach

        for i, h in enumerate(heights + [0]):   # +[0] = sztuczny słupek, by na końcu wyczyścić stos
            while stack and heights[stack[-1]] > h:
                top   = stack.pop()             # indeks ostatniego *wyższego* słupka
                right = i                       # bieżący indeks jest pierwszą mniejszą wysokością z prawej
                left  = stack[-1] if stack else -1   # po popie: pierwsza mniejsza z lewej (-1 gdy brak)

                width = right - left - 1       # ile kolumn obejmie prostokąt
                area  = heights[top] * width    # wysokość(top) × szerokość

                maxArea = max(maxArea, area)    # aktualizacja rekordu

            stack.append(i)                     # dodaj bieżący słupek (zachowując rosnące heights)

        return maxArea


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, elem in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > elem:
                top = stack.pop()
                left = stack[-1] if stack else -1
                wight = i - left -1
                area = wight * heights[top]
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
    
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                left = stack[-1] if stack else -1
                wight = i - left -1
                area = wight * heights[top]
                max_area = max(max_area, area)
            
            stack.append(i)
        
        return max_area
    

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                left = stack[-1] if stack else -1
                w = i - left -1
                a = w * heights[top]
                max_area = max(a, max_area)
            stack.append(i)
        return max_area