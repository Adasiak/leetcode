from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not (s or p):
            return []
        counter = Counter(p)
        size_of_window = len(p)
        res = []
        for i in range(len(s) - size_of_window + 1):
            tmp =  s[i: i + size_of_window]
            tmp_counter = Counter(tmp)                    
            if tmp_counter == counter:
                res.append(i)
        return res
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not (s or p):
            return []
        size_of_window = len(p)
        tmp_p = sorted(p)
        res = []
        for i in range(len(s) - size_of_window + 1):
            tmp =  s[i: i + size_of_window]
            tmp_sorted = sorted(tmp)                    
            if tmp_sorted == tmp_p:
                res.append(i)
        return res
    

# OPtymalne wersje 



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        need = Counter(p)
        window = Counter(s[:len(p)])

        if window == need:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            # usuń znak wychodzący z lewego końca
            left_char = s[i-1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            # dodaj nowy znak z prawej
            right_char = s[i + len(p) - 1]
            window[right_char] += 1

            if window == need:
                res.append(i)

        return res
    
    
    
    

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        have = Counter(s[:len(p)])
        need = Counter(p)
        
        if need == have:
            res.append(0)
        
        for i in range(1, len(s) - len(p) + 1):
            left_s = s[i-1] 
            have[left_s] -= 1
            right = s[i+ len(p) - 1]
            have[right] += 1
            if need == have:
                res.append(i)
        return res