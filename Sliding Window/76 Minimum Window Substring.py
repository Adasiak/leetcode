from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need   = Counter(t)           # wymagane częstotliwości
        have   = Counter()
        formed = 0                    # ile liter spełnia warunek
        req    = len(need)            # liczba różnych liter w t
        
        best_len = float('inf')
        best_l   = 0
        
        left = 0
        for right, ch in enumerate(s):
            # 1. rozszerz prawe
            have[ch] += 1
            if ch in need and have[ch] == need[ch]:
                formed += 1
            
            # 2. zwężaj lewe, gdy okno spełnia warunek
            while formed == req:
                # zaktualizuj wynik
                win_len = right - left + 1
                if win_len < best_len:
                    best_len = win_len
                    best_l   = left
                
                # usuń s[left] z okna
                left_ch = s[left]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1
        
        return "" if best_len == float('inf') else s[best_l:best_l + best_len] 
    

from collections import Counter, defaultdict
from typing import Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # 1. policz, czego potrzebujemy
        need = Counter(t)                # np.  {"A":1,"B":1,"C":1}
        have = defaultdict(int)          # bieżące częstotliwości w oknie
        need_types = len(need)           # ile różnych liter musimy spełnić
        have_types = 0                   # ile już spełniliśmy

        best_len = float("inf")          # długość najlepszego okna
        best_l: Tuple[int, int] = (0, 0) # jego indeksy [l, r+1)

        l = 0                            # lewy kraniec okna
        for r, ch in enumerate(s):       # prawy kraniec rośnie
            if ch in need:               # litery spoza 't' ignorujemy
                have[ch] += 1
                if have[ch] == need[ch]:
                    have_types += 1      # ta litera w pełni zaspokojona

            # gdy wszystkie typy liter spełnione, próbujemy zwęzić okno
            while have_types == need_types:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = (l, r + 1)  # +1 bo przekrój w Pythonie jest [l:r)

                pop_char = s[l]          # usuwamy znak z lewej
                if pop_char in need:
                    have[pop_char] -= 1
                    if have[pop_char] < need[pop_char]:
                        have_types -= 1  # już nie spełniamy wymagań
                l += 1                   # zwęż okno od lewej

        return "" if best_len == float("inf") else s[best_l[0]:best_l[1]]


  
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        have = defaultdict(int)
        need_types = len(need)
        have_types = 0
        best_len = float("inf")
        best_l = (0, 0)
        l = 0
        for r, char in enumerate(s):
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    have_types += 1
            
            while have_types == need_types:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = (l, r+1)
                
                pop_char = s[l]
                if pop_char in need:
                    have[pop_char] -= 1
                    if have[pop_char] < need[pop_char]:
                        have_types -= 1
                l += 1
        return "" if best_l == float("inf") else s[best_l[0]:best_l[1]]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        need_types = len(need)
        have_types = 0
        best_len = float("inf")
        best_l = (0, 0)
        l = 0
        for r, char in enumerate(s):
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    have_types += 1
            
            while have_types == need_types:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = (l, r+1)
                
                pop_char = s[l]
                if pop_char in need:
                    have[pop_char] -= 1
                    if have[pop_char] < need[pop_char]:
                        have_types -= 1
                l += 1
        return "" if best_len == float("inf") else s[best_l[0]:best_l[1]]
    
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        have_types = 0
        need_types = len(need)
        best_len = float("inf")
        res = ""
        l = 0
        
        for r, char in enumerate(s):
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    have_types += 1
            
            while have_types == need_types:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    res = s[l:r+1]
                
                pop_char = s[l]
                if pop_char in need:
                    have[pop_char] -= 1
                    if have[pop_char] < need[pop_char]:
                        have_types -= 1
                l += 1
        return res
    
    
    

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        have_types = 0
        need_types = len(need)
        best_len = float("inf")
        res = ""
        i = 0
        for r, char in enumerate(s):
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    have_types += 1
            
            while have_types == need_types:
                if r - i + 1 < best_len:
                    best_len = r - i + 1
                    res = s[i: r+1]
                pop_char = s[i]
                if pop_char in have:
                    have[pop_char] -= 1
                    if have[pop_char] < need[pop_char]:
                        have_types -= 1
                i += 1
        return res