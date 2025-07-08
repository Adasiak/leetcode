from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MODULO = 10**9 + 7
        if not(words or target):
            return 0
        w, t = len(words[0]), len(target)
        dp = [[0] * (t + 1) for _ in range(w + 1)]
        for j in range(1, t + 1):
            dp[0][j] = 1
            
        for i in range(t):
            for j in range(w):
                
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1] * counts[j-1][target[i-1]]) % MODULO
                
        return dp[len(target)][w]
    
    
from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # Modulo do unikania przepełnienia liczb
        MOD = 10**9 + 7
        
        # Długość słowa docelowego
        m = len(target)
        # Długość każdego słowa w słowniku (zakładamy, że wszystkie słowa mają tę samą długość)
        k = len(words[0])
        
        # 1. Przygotowanie danych: policz wystąpienia każdej litery na każdej pozycji.
        # 'char_counts[col_idx][char_code]' przechowuje liczbę wystąpień 'char_code'
        # na pozycji 'col_idx' we wszystkich słowach.
        # Używamy defaultdict(int) dla wygody, aby domyślna wartość dla nieobecnej litery była 0.
        char_counts = [defaultdict(int) for _ in range(k)]
        
        for word in words:
            for col_idx, char in enumerate(word):
                char_counts[col_idx][char] += 1
                
        # 2. Inicjalizacja tablicy DP.
        # dp[i][j] będzie przechowywać liczbę sposobów na utworzenie prefiksu target
        # o długości 'i' (target[0...i-1]), używając liter z pierwszych 'j' kolumn.
        # Rozmiar (m + 1) x (k + 1)
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        
        # Inicjalizacja bazowa: Jest 1 sposób na utworzenie pustego stringa (prefiks długości 0)
        # niezależnie od liczby rozważanych kolumn.
        for j in range(k + 1):
            dp[0][j] = 1
            
        # 3. Wypełnianie tablicy DP.
        # Iterujemy przez długość prefiksu 'target' (od 1 do m)
        for i in range(1, m + 1):
            # Iterujemy przez kolumny (od 1 do k)
            # Kolumna 'j' w dp odpowiada kolumnie 'j-1' w char_counts i słowach.
            for j in range(1, k + 1):
                
                # Opcja 1: Nie używamy litery z bieżącej kolumny (j-1) do zbudowania target[i-1].
                # Liczba sposobów jest taka sama, jak gdybyśmy rozważali tylko j-1 kolumn.
                dp[i][j] = dp[i][j-1]
                
                # Opcja 2: Używamy litery z bieżącej kolumny (j-1) do zbudowania target[i-1].
                
                # Litera, której potrzebujemy dla bieżącej pozycji w target.
                required_char = target[i-1]
                
                # Liczba wystąpień tej litery w bieżącej kolumnie (j-1).
                # Jeśli litera nie występuje, char_counts[j-1][required_char] będzie 0.
                count_of_required_char = char_counts[j-1][required_char]
                
                # Aby użyć tej litery, musieliśmy wcześniej zbudować prefiks target[0...i-2]
                # za pomocą (j-1) kolumn. Liczba sposobów na to to dp[i-1][j-1].
                # Mnożymy to przez liczbę wystąpień 'required_char' w bieżącej kolumnie.
                ways_if_using_current_char = (count_of_required_char * dp[i-1][j-1]) % MOD
                
                # Dodajemy tę opcję do ogólnej liczby sposobów dla dp[i][j].
                dp[i][j] = (dp[i][j] + ways_if_using_current_char) % MOD
                
        # 4. Wynik końcowy to liczba sposobów na utworzenie całego 'target' stringa,
        # używając wszystkich 'k' kolumn.
        return dp[m][k]
    
    
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        
        m = len(target)
        k = len(words[0])
        
        char_counts = [defaultdict(int) for _ in range(k)]
        
        for word in words:
            for col_idx, char in enumerate(word):
                char_counts[col_idx][char] += 1
                
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        
        for j in range(k + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j-1]
                required_char = target[i-1]
                count_of_required_char = char_counts[j-1][required_char]
                ways_if_using_current_char = (count_of_required_char * dp[i-1][j-1]) % MOD
                dp[i][j] = (dp[i][j] + ways_if_using_current_char) % MOD
        return dp[m][k]
    
    
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        k, m = len(words[0]), len(target)
        
        char_counts = [defaultdict(int) for _ in range(k)]
        
        for word in words:
            for i, v in enumerate(word):
                char_counts[i][v] += 1
                
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        
        for j in range(k + 1):
            dp[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j - 1]
                reqired_char = target[i - 1]
                count_of_required_char = char_counts[j - 1][reqired_char]
                ways_is_using_current_char = (count_of_required_char * dp[i - 1][j - 1]) % MOD
                dp[i][j] = (dp[i][j] + ways_is_using_current_char) % MOD
        return dp[-1][-1]
    
    
    
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        k, m = len(target), len(words[0])
        
        chars_counter = [defaultdict(int) for _ in range(m + 1)]
        for word in words:
            for i, v in enumerate(word):
                chars_counter[i][v] += 1
        
        dp = [[0] * (k + 1) for _ in range(m + 1) ]
        
        for j in range(k + 1):
            dp[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j - 1]
                required_char = target[i - 1]
                coun_of_required_char = chars_counter[j - 1][required_char]
                ways_is_using_current_char = (coun_of_required_char * dp[i -1][j - 1]) % MOD
                dp[i][j] = (dp[i][j] + ways_is_using_current_char) % MOD
        return dp[-1][-1]


























    
    
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        w, t = len(words[0]), len(target)
        
        char_counter = [defaultdict(int) for _ in range(w)]
        for word in words:
            for i, v in enumerate(word):
                char_counter[i][v] += 1
        
        dp = [[0] * (w + 1) for _ in range(t + 1)]
        
        for j in range(w + 1):
            dp[0][j] = 1
        
        for i in range(1, t + 1):
            for j in range(1, w + 1):
                dp[i][j] = dp[i][j - 1]
                required_char = target[i - 1]
                coun_of_required_char = char_counter[j - 1][required_char]
                ways = (coun_of_required_char * dp[i - 1][j - 1]) % MOD
                dp[i][j] = (dp[i][j] + ways) % MOD
                    
        return dp[-1][-1]
    
    
    

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD  = 10**9 + 7
        w, t = len(words[0]), len(target)
        
        char_counter = [defaultdict(int) for _ in range(w)]
        
        for word in words:
            for i, v in enumerate(word):
                char_counter[i][v] += 1
                
        dp = [[0] * (w + 1) for _ in range(t + 1)]
        
        for j in range(w + 1):
            dp[0][j] = 1
            
        for i in range(1, t + 1):
            for j in range(1, w + 1):
                dp[i][j] = dp[i][j - 1]
                require_char = target[i - 1]
                counter = char_counter[j - 1][require_char]
                ways = (counter * dp[i - 1][j - 1]) % MOD
                dp[i][j] = (ways + dp[i][j]) % MOD
        return dp[-1][-1]