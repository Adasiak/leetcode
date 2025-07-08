class Solution:
    def maxProduct(self, s: str) -> int:
        pass
        
        
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromes = {}  # Słownik: maska -> długość

        # 1. Generujemy wszystkie palindromiczne podciągi
        for mask in range(1, 1 << n):  # 1 << n to 2^n
            subsequence = ""
            for i in range(n):
                if (mask >> i) & 1:  # Sprawdzamy, czy i-ty bit jest ustawiony
                    subsequence += s[i]
            
            if subsequence == subsequence[::-1]:
                palindromes[mask] = len(subsequence)

        max_prod = 0
        
        # 2. Szukamy dwóch rozłącznych masek
        # Konwertujemy na listę, by łatwiej iterować po parach
        masks = list(palindromes.keys())
        for i in range(len(masks)):
            for j in range(i, len(masks)):
                mask1 = masks[i]
                mask2 = masks[j]
                
                # Sprawdzamy rozłączność masek
                if (mask1 & mask2) == 0:
                    product = palindromes[mask1] * palindromes[mask2]
                    max_prod = max(max_prod, product)

        return max_prod
    
    
    
    
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        self.max_product = 0

        def is_palindrome(text: str) -> bool:
            return text == text[::-1]

        def backtrack(index: int, sub1: str, sub2: str):
            # Warunek bazowy: przeanalizowaliśmy cały string
            if index == n:
                if is_palindrome(sub1) and is_palindrome(sub2):
                    self.max_product = max(self.max_product, len(sub1) * len(sub2))
                return

            # Krok rekurencyjny - 3 wybory dla s[index]
            
            # 1. Dodaj do pierwszego podciągu
            backtrack(index + 1, sub1 + s[index], sub2)
            
            # 2. Dodaj do drugiego podciągu
            backtrack(index + 1, sub1, sub2 + s[index])
            
            # 3. Zignoruj
            backtrack(index + 1, sub1, sub2)

        backtrack(0, "", "")
        return self.max_product
    
    
def 