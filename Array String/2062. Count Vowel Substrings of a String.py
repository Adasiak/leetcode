class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if not word:
            return 0
        vowel_substring = ['a', 'e', 'i', 'o', 'u']
        i = 0
        ll = len(word)
        res = []
        while True:
            if ll - i < len(vowel_substring):
                break
            if word[i] in vowel_substring:
                for j in range(i + 1, ll):
                    if word[j] not in vowel_substring:
                        break
                    tmp = word[i :j + 1]
                    if "a" in tmp and "e" in tmp and "i" in tmp and "o" in tmp and "u" in tmp:
                        res.append(tmp)
            i += 1
        return len(res)
    
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if not word:
            return 0
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        count = 0
        
        # Iterujemy przez każdy możliwy początek podciągu
        for i in range(n):
            # Resetujemy zestaw znalezionych samogłosek dla nowego podciągu
            current_vowels = set() 
            # Iterujemy przez każdy możliwy koniec podciągu, zaczynając od i
            for j in range(i, n):
                char = word[j]
                # Jeśli znak nie jest samogłoską, to ten podciąg i wszystkie dłuższe zaczynające się od i, a zawierające ten znak, nie mogą być podciągami samogłoskowymi.
                if char not in vowels:
                    break
                
                current_vowels.add(char)
                
                # Jeśli znaleźliśmy wszystkie 5 samogłosek, zwiększamy licznik
                if len(current_vowels) == 5:
                    count += 1
                    
        return count