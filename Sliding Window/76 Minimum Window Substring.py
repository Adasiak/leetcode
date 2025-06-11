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
    
    
class Solution:
    def minWindow(self, s: str, t: str) -> str: