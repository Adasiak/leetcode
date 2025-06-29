from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        have = defaultdict(int)
        need = Counter(t)
        have_type = 0
        need_type = len(need)
        res = ""
        best_len = float("inf")
        i = 0
        
        for right in range(len(s)):
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    have_type += 1
                
            while have_type == need_type:
                if len(s[i :right + 1]) < best_len: 
                    best_len = len(s[i :right + 1])
                    res = s[i:right + 1]
                
                left = s[i]
                if left in need:
                    have[left] -= 1
                    if have[left] < need[left]:
                        have_type -= 1
                i += 1
        return res