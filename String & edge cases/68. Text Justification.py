from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        space = 0
        res = []
        tmp = []
        len_of_words = 0
        i = 0
        len_of_wordss = len(words)
        passs = True
        while i <= len_of_wordss:
            if i < len_of_wordss and ((not len_of_words and len(words[i]) <= maxWidth) or (len_of_words and len_of_words + 1 + len(words[i]) <= maxWidth)):
                len_of_words += len(words[i])
                tmp.append(words[i])
                if len(tmp) >= 2:
                    len_of_words += 1
                i += 1
                print(i)
            else:
                tmp_str = ""
                if i + 1 != len(words):
                    tmp_len = len(tmp)
                    needed_space = tmp_len - 1
                    len_of_words_without_space = len_of_words - needed_space
                    all_needed_space = maxWidth - len_of_words_without_space
                    
                    for j in range(len(tmp)):
                        tmp_str += tmp[j]
                        if j + 1 != len(tmp):
                            print(j, "KURWA")
                            neede_for_one_space = (all_needed_space + needed_space - 1) // needed_space
                            spaces = " " * neede_for_one_space
                            tmp_str += spaces
                        
                            all_needed_space -= neede_for_one_space
                            needed_space -= 1
                            print(tmp, tmp[j], j, len(tmp), needed_space)
                else:
                    last_space = maxWidth - len_of_words
                    for q in range(len(tmp)):
                        tmp_str += tmp[q]
                        if q + 1 != len(tmp):
                            spaces = " " * last_space
                        else:
                            spaces = " "
                        tmp_str += spaces

                res.append(tmp_str)
                tmp = []
                len_of_words = 0
                
        return res        
                
            
            
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res: List[str] = []
        i, n = 0, len(words)

        while i < n:
            # ---------- 1) zbierz słowa, które mieszczą się w bieżącym wierszu ----------
            j, line_len = i, 0
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1          # j jest pierwszym słowem, które się NIE zmieści

            gaps = j - i - 1     # liczba przerw między słowami w linii

            # ---------- 2) zbuduj wiersz ----------
            if j == n or gaps == 0:          # ostatnia linia lub pojedyncze słowo
                line = ' '.join(words[i:j])  # pojedyncze spacje pomiędzy
                line += ' ' * (maxWidth - len(line))   # padding na koniec
            else:                            # linia w pełni justowana
                spaces = maxWidth - line_len           # ile łącznie spacji trzeba wstawić
                base, extra = divmod(spaces, gaps)     # extra dostaje pierwszych „extra” przerw

                line_parts = []
                for k in range(i, j - 1):
                    line_parts.append(words[k])
                    # podstawowych „base” spacji + ewentualnie jedna ekstra
                    line_parts.append(' ' * (base + (1 if k - i < extra else 0)))
                line_parts.append(words[j - 1])        # ostatnie słowo
                line = ''.join(line_parts)

            res.append(line)
            i = j                                       # zaczynamy nową linię

        return res
